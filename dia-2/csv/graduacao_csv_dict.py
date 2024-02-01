import csv

# IMPORTANTE
# Nesse eu não preciso desempacotar como no outro:
# header, *data = group_by_department DEPOIS da linha 9

# lê os dados
with open("dia-2/csv/graduacao_unb.csv", encoding = "utf-8") as file:
    graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')

    # A linha de cabeçalhos é utilizada como chave do dicionário
    # agrupa cursos por departamento
    group_by_department = {}
    for row in graduacao_reader:
        department = row["unidade_responsavel"]
        if department not in group_by_department:
            group_by_department[department] = 0
        group_by_department[department] += 1

# print(group_by_department)

# Escreve o relatório em .csv
# Abre um arquivo para escrita
with open("dia-2/csv/department_report_dict.csv", "w", encoding = "utf-8") as file:
    writer = csv.writer(file)

    # Escreve o cabeçalho
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    writer.writerow(headers)

    # Escreve as linhas de dados
    # Desempacotamento de valores
    for department, grades in group_by_department.items():
        # Agrupa o dado com o turno
        row = [
            department,
            grades,
        ]
        writer.writerow(row)