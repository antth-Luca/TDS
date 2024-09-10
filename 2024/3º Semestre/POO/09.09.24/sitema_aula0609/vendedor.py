from pessoa import Pessoa

class Vendedor(Pessoa):
    matricula = ""
    __salario = 0
    __pontos = 0

    def __init__(self, n, cpf, t, mat, sal):
        super().__init__(n, cpf, t)

        self.matricula = mat
        self.__salario = float(sal)
        self.__pontos = 0
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, sal):
        self.__salario = sal

    def get_pontos(self):
        return self.__pontos
    
    def set_pontos(self, pts):
        self.__pontos = pts

    def gerar_valores(self):
        self.__pontos += 2
