from tela import Tela
from vendedor import Vendedor
from cliente import Cliente

t = Tela()
vetor_vendedores = list()
vetor_clientes = list()

op = t.construir_tela()
while op != 0:
    # Criar vendedor
    if op == 1:
        encontrou = False
        response = None
        mat = input("Matricula vendedor:\n> ")
        for obj in vetor_vendedores:          
            if obj.matricula == mat:
                obj.gerar_valores()
                encontrou = True
                response = 'Valores atualizados!'
        if not encontrou:      
            nome = input("Nome vendedor:\n> ")
            cpf = input("CPF vendedor:\n> ")  
            v = Vendedor(nome, cpf, mat)
            v.gerar_valores()

            vetor_vendedores.append(v)
            response = 'Vendedor criado!'
        
        op = t.construir_tela(response)
    # Criar cliente
    elif op == 2:
        encontrou = False
        response = None
        n_fidel = input('Núm. Fidelidade:\n> ')
        for obj in vetor_clientes:
            if obj.n_fidelidade == n_fidel:
                obj.gerar_valores()
                encontrou = True
                response = 'Valores atualizados!'
        if not encontrou:
            nome = input("Nome cliente:\n> ")
            cpf = input("CPF cliente:\n> ") 
            c = Cliente(nome, cpf, n_fidel)
            c.gerar_valores()

            vetor_clientes.append(c)
            response = 'Cliente criado!'

        op = t.construir_tela(response)
    # Listar vendedores
    elif op == 3:
        print('===========================')
        for cont, obj in enumerate(vetor_vendedores, start=1):
            print(f'{cont}. {obj.nome} - matrícula: {obj.matricula}')
        
        print('> Para continuar, aperte Enter <')
        continuar = input() 
        op = t.construir_tela()
    # Listar clientes
    elif op == 4:
        print('===========================')
        for cont, obj in enumerate(vetor_clientes, start=1):
            print(f'{cont}. {obj.nome} - núm. fidelidade: {obj.n_fidelidade}')
        
        print('> Para continuar, aperte Enter <')
        continuar = input() 
        op = t.construir_tela()

# Opção de saída
t.limpar_terminal()

# Tabela de Vendedores
t.desenhar_tabela("Vendedores", vetor_vendedores, campos=['nome', 'matricula', 'pontos'])
print()

# Tabela de Clientes
t.desenhar_tabela("Clientes", vetor_clientes, campos=['nome', 'n_fidelidade', 'credito'])
print()

print(">> Até mais... <<")
