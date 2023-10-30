import json
import requests

APIkoodi = "7e2230b8bbfd3d666cee2f2835df9ffc"

paikkakunta = input("Anna paikkakunnan nimi: ")

pyyntö1 = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit=1&appid={APIkoodi}"
vastaus1 = requests.get(pyyntö1).json()
#print(json.dumps(vastaus1, indent=2))

lat = vastaus1[0]['lat']
lon = vastaus1[0]['lon']

pyyntö2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkoodi}"
vastaus2 = requests.get(pyyntö2).json()
#print(json.dumps(vastaus2, indent=2))

print(paikkakunta)
print(f"Säätila: {vastaus2['weather'][0]['main']}")
lämpötila = vastaus2['main']['temp'] - 273.15
print(f"Lämpötila: {lämpötila:0.2f} ºC")