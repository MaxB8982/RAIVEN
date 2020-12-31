import requests
from bs4 import BeautifulSoup

def isolate (url):
    req = requests.get(url = url, headers = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup.get_text()