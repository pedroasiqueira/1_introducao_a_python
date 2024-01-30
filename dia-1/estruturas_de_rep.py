pantheon_of_arton = [
    {"nome": "Wynna", "dominio": "Magia"},
    {"nome": "Nimb", "dominio": "Sorte"},
    {"nome": "Ahadarak", "dominio": "Tormenta"},
]

domains = []

for god in pantheon_of_arton:
    domains.append(god["dominio"])

# print("domains = ", domains)

# COMPREENSION:
domains_compreension = [god["dominio"] for god in pantheon_of_arton]

# print("domains_compreension = ", domains_compreension)

domains_compreension_without = [
    god for god in pantheon_of_arton if god["dominio"] != "Tormenta"
]
# print("domains_compreension_without = ", domains_compreension_without)

# Com o while nós podemos executar um conjunto de declarações enquanto a condição for verdadeira:
n = 10
last, next = 0, 1
while last < n:
    # print(last)
    last, next = next, last + next


# Em alguns casos, podemos ainda querer percorrer uma sequência numérica, e para isto iteramos sobre a estrutura de dados range.
# for index in range(1, 6):
#     print(index)