from e_Heranca_1 import Eletrodomestico

class Liquidificador(Eletrodomestico):
      def __str__(self):
        return f"""
        Detahes do liquidificador:
        - Cor: {self.cor}
        - Potencia: {self._potencia}
        - Tensao: {self._tensao}
        - Preco: {self.preco}
        """


liq = Liquidificador("Vermelho", "110", "127", "200")

print(liq)

class A:
    def faz_algo(self, valor):
        print(valor)


class B(A):
    def faz_outra_coisa(self):
        print("Vou printar o valor pelo método criado em A")
        # Chama o método da classe A, que neste caso é a superclasse, passando
        # o `self` explicitamente
        A.faz_algo(self, valor=1)
        #ou
        super().faz_algo(valor=2) #melhor
        #Mudar de acesso direto para super não somente não traz nenhum prejuízo como ainda traz uma melhoria: Se eu mudar a classe da qual B herda de A para qualquer outra que possua o método faz_algo, tudo continua a funcionar.


b = B()
b.faz_outra_coisa()
# Vou printar o valor pelo método criado em A
# 1