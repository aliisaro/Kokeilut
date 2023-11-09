import json
import requests

pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()
#print(json.dumps(vastaus, indent=2))
print(vastaus['value'])