import requests

URL = "https://neetcode.io/practice"

page = requests.get(URL)


print(page.encoding)
print(page.url)