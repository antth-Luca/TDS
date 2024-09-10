from pessoa import Pessoa

class Cliente(Pessoa):
    n_fidelidade = ''
    __credito = 0

    def __init__(self, n, c, f):
        super().__init__(n, c)
        self.n_fidelidade = f

    def get_credito(self):
        return self.__credito

    def gerar_valores(self):
        self.__credito += 10
