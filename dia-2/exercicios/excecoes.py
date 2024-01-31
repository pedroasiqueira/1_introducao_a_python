with open("dia-2/exercicios/arqCriados/notas.txt", "w") as notas:
    LINES = [
        "Marcos 10\n",
        'Felipe 4\n',
        'José 6\n',
        'Ana 10\n',
        'Maria 9\n',
        'Miguel 5\n',
    ]
    notas.writelines(LINES)


reprovados = []
with open("dia-2/exercicios/arqCriados/notas.txt", "r") as read_notas_file:
    for line in read_notas_file:
        nome, nota = line.split()
        if int(nota) < 6:
          reprovados.append(f'{nome}\n')


with open("dia-2/exercicios/arqCriados/repro.txt", "w") as reprovados_file:
    print(reprovados)
    reprovados_file.writelines(reprovados)