from pessoa import Pessoa

class Vendedor(Pessoa):
    matricula = ''
    __salario = 0
    __pontos = 0

    def __init__(self, n, c, m):
        super().__init__(n, c)  
        self.matricula = m

    def get_salario(self):
        return self.__salario

    def set_salario(self, s):
        self.__salario = s

    def get_pontos(self):
        return self.__pontos

    def gerar_valores(self):
        self.__pontos += 2
