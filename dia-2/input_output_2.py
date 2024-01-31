import sys


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)

# digitar no terminal: python3 dia-2/input_2.py 2 4 "teste"

#formas de chamar o print
# print("Os resultados são", 6, 23, 42, sep=" - ")  # saída: Os resultados são * 6 * 23 * 42

err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)