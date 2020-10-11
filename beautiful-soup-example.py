import urllib.request
from bs4 import BeautifulSoup

url = input("Enter - ")
print(url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
