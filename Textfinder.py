import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

def isolate (url):
    req = urllib.request.Request(url = url, headers = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    response = urllib.request.urlopen(req)
    soup = BeautifulSoup(response.read(), 'html.parser')
    return soup.get_text()