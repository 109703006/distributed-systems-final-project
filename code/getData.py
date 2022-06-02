import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}
r = requests.get("https://zxc22.idv.tw/sche/main.asp?clickflag=999", headers=headers)
r.encoding = "big5"
# print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
table = soup.find_all("td", align="center", bgcolor="white", valign="top")
for element in table:
    print(element)
for element in table:
    print(element.getText())
