from tabulate import tabulate

titles = ["Animes", "Temporadas"]
data = [
    ["Mashle", 1],
    ["Spy Family", 1],
    ["Jujutsu Kaisen", 2],
    ["Attack on Titan", "infinitas"],
]

print(tabulate(data, headers=titles, tablefmt="fancy_grid", numalign="center"))