import requests

respons = requests.get("https://www.ceneo.pl/96796516#tab=reviews")

print(respons.text)