my_array = [20, 20, 1, 2]

freq_dict = {}

for item in my_array:
    if (item in freq_dict):
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1

for key, valor in freq_dict.items():
    print(f"{key} : {valor}")

# para uma dict ficar iteravel, acho que funciona com o set() tbm
print(freq_dict.items())

# Saída
#20: 2
#1: 1
#2: 1