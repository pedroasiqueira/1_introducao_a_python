a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

teste, teste1 = 'ef', 'g'
print(teste)
print(teste1)

head, *tail = (
    1,
    2,
    3,
)  # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]


x = "ab"
x, y = "ab"
# Saída:
# x = "a"; y = "b"

nome_e_nascimento = [("Felps", "México"), ("João", "Brasil")]
for nome, pais in nome_e_nascimento:
    print(nome, pais)
# Saída:
# Felps Máxico
# João Brasil

x, y = "Felps"
# Saída:
# ValueError: too many values to unpack

x, *y = "Felps"
# Saída:
# x = "F"
# y = ["e", "l", "p", "s"]

x, *y = "Felps"
# Saída:
# x = "F"
# y = ["e", "l", "p"]
# z = "s"