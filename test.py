import requests
from bs4 import BeautifulSoup

#TODO figure out how to get the proper html to show exactly how it does on the web browser
#TODO figure out what framework is being used, in order to properly emulate the page being shown
URL = "https://neetcode.io/practice"

page = requests.get(URL)


print(page.encoding)
print(page.url)
print()

soup = BeautifulSoup(page.text, 'lxml')
print(soup.prettify() )

