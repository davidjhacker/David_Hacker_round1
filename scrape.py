import requests
import json
import emoji
from bs4 import BeautifulSoup
def bify(word):
    b = list(word)
    b[0] = "🅱️"
    b = "".join(b)
    return b
page = requests.get("https://www.thecrimson.com/")
soup = BeautifulSoup(page.content, 'html.parser')
headlines = []
for headline in soup.find_all("h1"):
    headlines.append(headline.get_text())
headlines.remove("Sections")
headlines.remove("About")
headlines.remove("Resources")
f = open("davidoutput.txt", "w")
for headline in headlines:
    f.write(headline + " --> ")
    for word in headline.split():
        page = requests.get("https://api.datamuse.com/words?ml=" + word + "&sp=b*&max=10")
        dictlist = json.loads(page.content)
        if word == "Harvard":
            f.write("🅱️arvard ")
        elif word == "of" or word == "on":
            f.write(word + " ")
        elif len(dictlist) == 0:
            f.write(word + " ")
        else:
            f.write(bify(dictlist[0]["word"]) + " ")
    f.write("\n")
f.close()
