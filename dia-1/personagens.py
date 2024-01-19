characters_file = open("meus-personagens.txt", mode="w")

characters_file.write("Naruto\n")
characters_file.write("Sasuke\n")
characters_file.write("Itachi\n")

print("Yusuke\n", file=characters_file)

more_characters = ["Gon\n", "Kilua\n"]

characters_file.writelines(more_characters)

characters_file.close()