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
