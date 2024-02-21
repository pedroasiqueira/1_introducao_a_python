import random

random_list = random.sample(range(0, 100000), 1000)

print(len(random_list))  # Saída: 1000
print(max(random_list))
print(min(random_list))
