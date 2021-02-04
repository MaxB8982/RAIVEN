from datetime import datetime
from dateutil import relativedelta
import urllib.request, urllib.error, urllib.parse

def compute (url):
    #find the exact source in google
    request_str = "https://www.google.com/search?q=inurl:{0}&as_qdr=y25".format(url)
    #pretend to be firefox so google doesn't block us
    req = urllib.request.Request(url = request_str, headers = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    #open the website
    response = urllib.request.urlopen(req)
    #record all the stuff on teh website in webContent
    webContent = str(response.read())
    #search for this class for the publish date
    x = webContent.find('class="f"')
    # websites with dates in google:
    if (x >= 0):
        y = webContent[x+10:]
        #is the word days in those digits?
        b = y.find('days')
        #if it isn't...
        if (b == -1):
            w = y.find(" ", 11)
            date = y[0:w]
            num_date = datetime.strptime(date,'%b %d, %Y')
            now = datetime.now()
            time_difference = relativedelta.relativedelta(now, num_date)
            difference_in_years = time_difference.years
            if (difference_in_years <= 0):
                return 10
            elif (difference_in_years <= 2):
                return 8
            elif (difference_in_years <= 4):
                return 6
            elif (difference_in_years <= 6):
                return 4
            elif (difference_in_years < 6 ):
                return 2
            else:
                return int(-1)
        #If there is the word days...
        elif (b >= 0):
            #give the source and A
            return 10
    # CNN articles
    elif (x == int(-1)):
        #<p class="update-time">Updated 3:51 PM ET, Tue January 19, 2021 <span id="js-pagetop_video_source" class="video__source top_source"></span></p>
        xCNN = webContent.find('<p class="update-time">')
        if (xCNN >= 0):
            yCNN = webContent[xCNN+25:]
            wCNN = yCNN.find(" ", 17)
            date = yCNN[0:wCNN]
            num_date = datetime.strptime(date,'%b %d, %Y')
            now = datetime.now()
            time_difference = relativedelta.relativedelta(now, num_date)
            difference_in_years = time_difference.years
            if (difference_in_years <= 0):
                return 10
            elif (difference_in_years <= 2):
                return 8
            elif (difference_in_years <= 4):
                return 6
            elif (difference_in_years <= 6):
                return 4
            elif (difference_in_years < 6 ):
                return 2
            else:
                return int(-1)
            # other article    
        elif (xCNN == int(-1)):
            return int(-1)