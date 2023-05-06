from lib.interface import *
from lib.arquivo import *

#Nomeando o arquivo de texto.
#Já existe um txt de teste, nome: "testes.txt"
arq = 'textoParaLer.txt'

#Aqui o algoritmo vai verificar se o arquivo de texto existe, caso não ele criará
if not arquivoExiste(arq):
    criarArquivo(arq)

                #Menu
while True:
    resp = menu(['Ler texto', 'Adicionar texto', 'Chamar incessantemente', 'Sair'])
    if resp == 1:
        #Opção para ler texto
        ler(arq)
    elif resp == 2:
        #Opção para adicionar um texto
        cabeçalho('ADICIONANDO TEXTO')
        texto = str(input('-> '))
        escrever(arq, texto)
    elif resp == 3:
        nome = str(input('Qual nome devo chamar?\n-> ')).strip().capitalize()
        chamar(nome)
    elif resp == 4:
        #Opção para encerrar
        cabeçalho('Encerrando... Programa finalizado!')
        voz.say('Obrigado por usarem um programa de Luca Anthony. Boa noite')
        voz.runAndWait()
        break
    else:
        #Se digitar algo diferente de 1, 2 ou 3 vem para cá...
        print('\033[31mERRO! Digite uma opção válida\033[m')
