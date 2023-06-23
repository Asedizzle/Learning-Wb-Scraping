import urllib.request,urllib.parse,urllib.error, ssl
from bs4 import BeautifulSoup

abc = ssl.create_default_context()
abc.check_hostname = False
abc.verify_mode = ssl.CERT_NONE

try:
   url = input("Please type a valid url")
   if len(url) < 1:
      url = "http://quotes.toscrape.com/"
      
   html = urllib.request.urlopen(url, context=abc).read()
   soup = BeautifulSoup(html, "lxml")
   
   quotes = soup.find_all("div", {"class":"quote"})
   for quote in quotes:
      print(quote.get_text())


except:
    print("Something went wrong")