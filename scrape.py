import requests
import json
import sys
from bs4 import BeautifulSoup
if len(sys.argv) != 2:
    sys.exit("Input number")
if float(sys.argv[1]) < 1 or float(sys.argv[1]) > 10:
    sys.exit("number must be between 1 and 10")
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
        elif word[0] == "b" or word[0] == "B":
            f.write(bify(word) + " ")
        else:
            is_good_word = False
            for dict in dictlist:
                if "score" not in dict.keys():
                    pass
                elif dict["score"]  > 100000 - (10000 * float(sys.argv[1])):
                    is_good_word = True
                    f.write(bify(dict["word"]) + " ")
                    break
            if is_good_word == False:
                f.write(word + " ")
    f.write("\n")
f.close()
