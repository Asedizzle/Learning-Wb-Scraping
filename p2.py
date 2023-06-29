#This code scrapes bookstoscrape.com and retrieves the titles of books available
import urllib.request,urllib.parse,urllib.error, ssl
from bs4 import BeautifulSoup
abc = ssl.create_default_context()
abc.check_hostname = False
abc.verify_mode = ssl.CERT_NONE

url = "http://books.toscrape.com/"
html = urllib.request.urlopen(url,context=abc).read()

soup = BeautifulSoup(html)

#print(soup.prettify())

tags = soup.find_all("h3")
for tag in tags:
    #print(tag.prettify())
    a_tag = tag.a.text
    print(a_tag)