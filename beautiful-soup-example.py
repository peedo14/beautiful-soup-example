import urllib.request
from bs4 import BeautifulSoup

url = input("Enter URL (example - http://www.youtube.com ) : ")
try:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup("a")
    if len(tags) == 0:
        print("Cannot found link with tag <a> in", url)
        quit()
    for tag in tags:
        print(tag.get("href", None))
except:
    print("Something went wrong")
    quit()
