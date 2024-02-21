from random import randint

pantheon_of_arton = [
    {"nome": "Wynna", "dominio": "Magia"},
    {"nome": "Nimb", "dominio": "Sorte"},
    {"nome": "Ahadarak", "dominio": "Tormenta"},
]

dice_roll = randint(1, 20)

if dice_roll == 1:
    print("Vixe... Deu ruim!")
elif 2 <= dice_roll <= 15:
    print("Ahadarak, porque me atormentas!")
elif 16 <= dice_roll <= 19:
    print("Nimb, obrigado pela sorte!")
else:
    print("Agora ninguém me segura")
