# get libraries
import requests
from bs4 import BeautifulSoup

# make a request
r = requests.get('')

# how'd it go?
r.status_code

# Soup object
soup = BeautifulSoup(r.text, 'html.parser', from_encoding="utf-8")

# find quotes
quotes = []
for item in soup.find_all('p'):
    # try to see if attribute has text
    try:
    # pass otherwise
    except:
        pass

# print the out one by one every 5 seconds for fun
from time import sleep
