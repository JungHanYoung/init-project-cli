import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20190602'

html = requests.get(url)

bs = BeautifulSoup(html.text, 'html.parser')

# print(bs.prettify())

print(bs.select_one(
    "body iframe div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong"))
