with open("dia-2/with-arqCriados/with-write.txt", "w") as file:
    file.write("nome idade\n")

    file.write("Maria 45\n")
    file.write("Miguel 33\n")
    print("Túlio 22", file=file)
    print("Pedro 28", file=file)

    LINES = [
        "Alberto 35\n",
        "Betina 22\n",
        "João 42\n",
        "Victor 19\n",
    ]
    file.writelines(LINES)

# Várias formas de se escrever
    
#lendo o arquivo criado acima
with open("dia-2/with-arqCriados/with-write.txt", "r") as file:
    content = file.read()
    print(content)

with open("dia-2/with-arqCriados/with-write.txt", "r") as file:
    for line in file:
        print(line)