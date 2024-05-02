import requests
from bs4 import BeautifulSoup

base_url = "https://punchng.com/topics/sports/"
response = requests.get(base_url)

content = BeautifulSoup(response.text, 'html.parser')
for y in content.find_all("div", {"class": "post-content"}):
    print(y.text.strip())
    link = y.find("a")
    if link:
        print(link.get('href'))
