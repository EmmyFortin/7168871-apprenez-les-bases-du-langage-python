import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

title = soup.title.string
print( "Titre de la page", title)