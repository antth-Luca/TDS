def leiaInt(msg):  #Tipo um input, mas não da erro se não digitar o tipo que pede. Usado no menu
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return n


#Apenas construção de interface para reduzir o tamanho do programa principal...
def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opç = leiaInt('\033[32mSua opção: \033[m')
    return opç
