from pessoa import Pessoa

class Cliente(Pessoa):
    num_fidelidade = ""
    __credito = 0

    def __init__(self, n, cpf, t, num_fidel):
        super().__init__(n, cpf, t)

        self.num_fidelidade = num_fidel
        self.__credito = 0

    def get_credito(self):
        return self.__credito
    
    def set_credito(self, cred):
        self.__credito = cred

    def gerar_valores(self):
        self.__credito += 10
