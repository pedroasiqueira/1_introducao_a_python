class Liquidificador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self.potencia = potencia
        self.tensao = tensao
        self.ligado = False
        self.velocidade = 0
        self.velocidade_maxima = 3
        self.corrente_atual_no_motor = 0

meu_liquidificador = Liquidificador("Azul", 200, 127, 200)
seu_liquidificador = Liquidificador(
    cor="Vermelho", potencia=250, tensao=220, preco=100
)

print(meu_liquidificador.cor)
print(seu_liquidificador.ligado)