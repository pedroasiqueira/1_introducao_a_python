# Lendo o arquivo que criei acima
with open("dia-2/with-arqCriados/with-write.txt", "r") as file:
    content = file.read()

    print(content)

# Fazendo o FOR
with open("dia-2/with-arqCriados/with-write.txt", "r") as file:
    for line in file:
        print(line)
