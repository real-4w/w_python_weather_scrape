import requests
from bs4 import BeautifulSoup
# enter city name
city = "West Harbour, Auckland, New Zealand"
# create url - example https://www.google.com/search?q=%22+%22weather%22+%22West%20Harbour,%20Auckland,%20New%20Zealand%22
url = "https://www.google.com/search?q="+"weather"+city

# requests instance
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')

# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# this contains time and sky description
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# format the data
data = str.split('\n')
time = data[0]
sky = data[1]

# list having all div tags having particular clas sname
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# particular list with required data
strd = listdiv[5].text

# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]

# printing all the data
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)

