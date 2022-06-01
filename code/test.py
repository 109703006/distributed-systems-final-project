import requests
from bs4 import BeautifulSoup

r = requests.get("https://zxc22.idv.tw/sche/main.asp?clickflag=999")
r.encoding = "big5"

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
