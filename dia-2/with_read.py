# Lendo o arquivo que criei acima
with open("teste-gerenciador-de-contexto.txt", "r") as file:
    content = file.read()

    print(content)

# Fazendo o FOR
with open("teste-gerenciador-de-contexto.txt", "r") as file:
    for line in file:
        print(line)
