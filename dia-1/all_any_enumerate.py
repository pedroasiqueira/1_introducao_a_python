languages = ["Python", "Java", "JavaScript"]

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
# print(list(enumerate_prime))

# Fazendo um exemplo de outra forma, com enumerate e for
great_chest_players_ranking = ["magnus", "fabiano", "hikaru", "anand", "alireza"]
great_cpr = list(enumerate(great_chest_players_ranking, start=1))
print(great_cpr)

refa = []
# depois do 'in', eu poderia ter colocado também a 'great_cpr'
for index, players in enumerate(great_chest_players_ranking, start=1):
    # print(f'{index} - {players}')
    refa.append((players, index))

print(refa)


# nomes_1 = ["Felps", "Carlos", "Will", "Bux"]
# nomes_2 = ["Flávio", "Carlos", "Roni", ""]

# all(nomes_1)  # Saída: True
# all(nomes_2)  # Saída: False

# any(nomes_1)  # Saída: True
# any(nomes_2)  # Saída: True

# for item in enumerate(nomes_1):
#     print(item)
# # Saída:
# # (0, 'Felps')
# # (1, 'Carlos')
# # (2, 'Will')
# # (3, 'Bux')
