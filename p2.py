#This code scrapes books.toscrape.com and retrieves the titles of books available
import urllib.parse,urllib.request,urllib.error, ssl
from bs4 import BeautifulSoup

abc = ssl.create_default_context()
abc.check_hostname = False
abc.verify_mode = ssl.CERT_NONE

url = "http://books.toscrape.com/"
html = urllib.request.urlopen(url,context=abc).read()

soup = BeautifulSoup(html)

#print(soup.prettify())

tags = soup.find_all("h3")
for i in tags:
    a_tags = soup.find_all("a")
    for i in a_tags:
        if i.get("title") is None:
            continue
        title = i.get('title')
        print(title)
            