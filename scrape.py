import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.thecrimson.com/")
soup = BeautifulSoup(page.content, 'html.parser')
headlines = []
def sarcastic(string):
    output = string[0]
    for i in range (1, len(string)):
        if output[i-1].isupper():
            output += (string[i].lower())
        else:
            output += (string[i].upper())
    return output
for headline in soup.find_all("h1"):
    headlines.append(headline.get_text())
headlines.remove("Sections")
headlines.remove("About")
headlines.remove("Resources")
f = open("davidoutput.txt", "w")
for headline in headlines:
    f.write(sarcastic(headline) + "\n")
f.close()
