import requests
from bs4 import BeautifulSoup

base = "https://www.arise.tv/category/sports/"
n = range(0, 4)
response = (requests.get(base))
contents = BeautifulSoup(response.text, 'html.parser')

for data in contents.find_all("h3", {"class": "h6"}):
    link = ('href')

'article'