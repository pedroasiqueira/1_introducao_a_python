import json

# leitura de todos os pokemons
with open("dia-2/json/pokemons.json") as file:
    pokemons = json.load(file)["results"]

# Separamos somente os do tipo grama
grass_type_pokemons = []
for pokemon in pokemons:
    if "Grass" in pokemon["type"]:
        grass_type_pokemons.append(pokemon)


#ESCREVENDO NO JSON, PRIMEIRA FORMA
# Abre o arquivo para escrevermos apenas o pokemons do tipo grama
with open("dia-2/json/grass_pokemonss-primeira-forma.json", "w") as file:
    json_to_write = json.dumps(
        grass_type_pokemons
    )  # conversão de Python para o formato json (str)
    file.write(json_to_write)


#ESCREVENDO NO JSON, SEGUNDA FORMA
# abre o arquivo para escrita
with open("dia-2/json/grass_pokemons-segunda-forma.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)


#Aparentemente as duas formas escrevem igual o arquivo