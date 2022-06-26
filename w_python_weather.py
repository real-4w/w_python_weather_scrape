import requests
from bs4 import BeautifulSoup
# enter city name
city = "West Harbour, Auckland, New Zealand"

# create url
# https://www.google.com/search?q=%22+%22weather%22+%22West%20Harbour,%20Auckland,%20New%20Zealand%22
url = "https://www.google.com/search?q="+"weather"+city

# requests instance
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
