import requests 
from bs4 import BeautifulSoup
import time 
import urllib3
 
url = 'https://www.investing.com/equities/safaricom'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.findAll = 'a'