import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}
r = requests.get(
    "https://zxc22.idv.tw/sche/main.asp?mmm=5&place=&team=", headers=headers
)
r.encoding = "big5"

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
table = soup.find_all("td", align="center", bgcolor="white", valign="top")
# print(table)
month = "5"
for element in table:
    # day = "0"
    # team1 = "0"
    # team2 = "0"
    elements = element.getText().split(" ")
    # print(elements)
    # get date
    if len(elements[0]) == 4:
        day = elements[0][0]
    elif len(elements[0]) == 5:
        day = elements[0][0] + elements[0][1]
    else:
        continue
    # get game1
    game1 = elements[1]
    teams = game1.split("(", 1)[0]
    team1 = teams.split("-")[0]
    team2 = teams.split("-")[1]
    stadium = game1.split("(", 1)[1].split(")", 1)[0]
    score = game1.split("(", 1)[1].split(")", 1)[1].split("(", 1)[0]
    print(stadium, str(month) + "-" + str(day), team1 + ":" + team2, score)

    # get game2
    game2 = elements[2]
    if len(game2) < 12:
        continue
    # print(game2, len(game2))
    teams = game2.split("(", 1)[0]
    team1 = teams.split("-")[0]
    team2 = teams.split("-")[1]
    stadium = game2.split("(", 1)[1].split(")", 1)[0]
    score = game2.split("(", 1)[1].split(")", 1)[1].split("(", 1)[0]
    # print(team1, team2, stadium, score)
    print(stadium, str(month) + "-" + str(day), team1 + ":" + team2, score)
