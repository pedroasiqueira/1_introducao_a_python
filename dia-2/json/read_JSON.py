import json


with open("dia-2/json/pokemons.json") as file:
    pokemons = json.load(file)["results"]

print(pokemons[0])  # imprime o primeiro pokemon da lista
for nameP in pokemons:
    print(nameP["name"])
