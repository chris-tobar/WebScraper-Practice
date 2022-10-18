import requests
from bs4 import BeautifulSoup


URL = "https://neetcode.io/practice"

page = requests.get(URL)


print(page.encoding)
print(page.url)
print()

soup = BeautifulSoup(page.text, 'lxml')
print(soup.prettify() )

