import os

class Tela():
    def limpar_terminal(self):
        # Verifica o sistema operacional
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para Linux e macOS
            os.system('clear')

    def construir_tela(self, response=None):
        self.limpar_terminal()

        if response:
            print(f'>> {response} <<')

        print('===========================')
        print('= (1) Vendedor            =')
        print('= (2) Cliente             =')
        print('= (3) Listar vendedores   =')
        print('= (4) Listar clientes     =')
        print('= (0) Contabilizar e Sair =')
        print('===========================')
        opcao = int(input('Digite a opção:\n> '))
        return opcao
    
    # Função para definir a largura dos campos
    def ajustar_colunas(self, texto, largura):
        return texto[:largura].ljust(largura)

    # Função para desenhar a tabela
    def desenhar_tabela(self, tipo, vetor, campos):
        # Definindo os tamanhos das colunas
        nome_largura = 20
        matricula_largura = 12 if tipo == "Vendedores" else 18
        credito_largura = 8
        total_largura = 4 + nome_largura + matricula_largura + credito_largura + 13  # Calcula o tamanho total da tabela
        
        # Cabeçalho e título dinâmico
        if tipo == "Vendedores":
            print(f"{'=' * total_largura}")
            print(f"| {'#':<4} | {'Nome':<{nome_largura}} | {'Matrícula':<{matricula_largura}} | {'Crédito':<{credito_largura}} |")
        else:
            print(f"{'=' * total_largura}")
            print(f"| {'#':<4} | {'Nome':<{nome_largura}} | {'Núm. Fidelidade':<{matricula_largura}} | {'Crédito':<{credito_largura}} |")
        
        print("-" * total_largura)  # Linha separadora dinâmica

        # Desenhar cada linha da tabela
        for cont, obj in enumerate(vetor, start=1):
            if tipo == "Vendedores":
                linha = f"| {cont:<4} | {self.ajustar_colunas(obj.nome, nome_largura)} | {self.ajustar_colunas(obj.matricula, matricula_largura)} | {self.ajustar_colunas(str(obj.get_pontos()), credito_largura)} |"
            else:
                linha = f"| {cont:<4} | {self.ajustar_colunas(obj.nome, nome_largura)} | {self.ajustar_colunas(obj.n_fidelidade, matricula_largura)} | {self.ajustar_colunas(str(obj.get_credito()), credito_largura)} |"
            print(linha)
        
        print("=" * total_largura)  # Linha final dinâmica