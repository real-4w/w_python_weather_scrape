import requests
from bs4 import BeautifulSoup

#https://stackoverflow.com/questions/50422136/python-requests-with-wincertstore/57053415#57053415

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"

# enter city name
city = "West Harbour, Auckland, New Zealand"
# create url - example https://www.google.com/search?q=%22+%22weather%22+%22West%20Harbour,%20Auckland,%20New%20Zealand%22
url = "https://www.google.com/search?q="+"weather"+city

# requests instance
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE

# getting raw data
html = session.get(url, verify=True).content
soup = soup = BeautifulSoup(html, 'html.parser')

# store all results on this dictionary
result = {}
# extract region
result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
# extract temperature now
result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
# get the day and hour now
result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
# get the actual weather
result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text

# get the precipitation
result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
# get the % of humidity
result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
# extract the wind
result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

print(result)