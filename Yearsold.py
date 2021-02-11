from datetime import datetime
from dateutil import relativedelta
import urllib.request, urllib.error, urllib.parse
import urlchopper
 
def computeGradeBased(date):
    #THE PRESENT
    now = datetime.now()
    #what's the time difference between now and the date the article was published.
    time_difference = relativedelta.relativedelta(now, date)
    #use only the difference in years
    difference_in_years = time_difference.years
    if (difference_in_years <= 0):
        #A
        return 10
    elif (difference_in_years <= 2):
        #B
        return 8
    elif (difference_in_years <= 4):
        #C
        return 6
    elif (difference_in_years <= 6):
        #D
        return 4
    elif (difference_in_years < 6 ):
        #F
        return 2
    else:
        #There was an error
        return int(-1)

def compute (url):
    #find the exact source in google
    request_str = "https://www.google.com/search?q=inurl:{0}&as_qdr=y25".format(url)
    #pretend to be firefox so google doesn't block us
    req = urllib.request.Request(url = request_str, headers = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    #open the website
    response = urllib.request.urlopen(req)
    #record all the stuff on the website in webContent
    webContent = str(response.read())
    #search for this class for the publish date
    x = webContent.find('class="f"')
    # websites with dates in google:
    if (x >= 0):
        #everything after ten places from x = y
        y = webContent[x+10:]
        #is the word days in those digits?
        b = y.find('days')
        #if it isn't...
        if (b == -1):
            w = y.find(" ", 11)
            date = y[0:w]
            num_date = datetime.strptime(date,'%b %d, %Y')
            return computeGradeBased(num_date)
        #If there is the word days...
        elif (b >= 0):
            #give the source and A
            return 10
    # CNN articles
    elif (x == int(-1)):
        #<p class="update-time">Updated 3:51 PM ET, Tue January 19, 2021 <span id="js-pagetop_video_source" class="video__source top_source"></span></p>
        matches = urlchopper.extract_date(url)
        if len(matches) == 3:
           date = datetime.date(int(matches[0], matches [1], matches [2])) 
           time = datetime.time(0, 0, 0)
           datetime2 = datetime.combine(date, time)
           return computeGradeBased(datetime2)
        elif len(matches) != 3:
            return int(-1)