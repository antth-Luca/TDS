global user

def apresentar_result(result):
    print(f'O resultado da sua operação é: {result}')


def soma_nums():
    l = list()
    l.append(int(input('Digite o primeiro número:\n>>> ')))
    l.append(int(input('Digite o segundo número:\n>>> ')))
    apresentar_result(l[0] + l[1])

    
def sub_nums():
    l = list()
    l.append(int(input('Digite o primeiro número:\n>>> ')))
    l.append(int(input('Digite o segundo número:\n>>> ')))
    apresentar_result(l[0] - l[1])
    


def fat_num(n):
    if n==0:
        return 1
    if n > 0:    
        return n * fat_num(n - 1)       
    


def home():
    print('=====================MENU======================\n')
    user = str(input('Digite, como devemos te chamar?\n>>> '))
    opcao = int(input(f'Seja bem-vindo(a), {user}! Escolha uma opção:\n>>> '))
    print('[1] - Soma')
    print('[2] - Subtraçao')
    print('[3] - Fatoriar')
    print('[0] - Sair')

    if opcao == 1:
        soma_nums()

    elif opcao == 2:
        sub_nums()

    elif opcao == 3:
        fat_num()

    elif opcao == 0:
        break


# Main Code
while (True):
    home()
    print('\nObrigado por usar o sistema de Not Real World!')
    print('===============================================')