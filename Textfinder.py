import requests
from bs4 import BeautifulSoup

def isolate (url):
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    for script in soup ('script'):
        script.decompose()