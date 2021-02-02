from datetime import datetime
from dateutil import relativedelta
import urllib.request, urllib.error, urllib.parse

def compute (url):
    request_str = "https://www.google.com/search?q=inurl:{0}&as_qdr=y25".format(url)
    req = urllib.request.Request(url = request_str, headers = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    response = urllib.request.urlopen(req)
    webContent = str(response.read())
    x = webContent.find('class="f"')
    # websites with dates in google
    if (x >= 0):
        y = webContent[x+10:]
        b = y.find('days')
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
        elif (b >= 0):
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