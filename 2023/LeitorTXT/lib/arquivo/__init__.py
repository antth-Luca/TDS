from lib.interface import *
import pyttsx3

#Preparando a voz que fará a leitura
voz = pyttsx3.init()

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo "{nome}" criado com sucesso!')


def ler(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro na leitura')
    else:
        cabeçalho('Lendo...')
        for linha in a:
            voz.say(linha)
            voz.runAndWait()
    finally:
        a.close()


def escrever(nomeArq, txt):
    try:
        a = open(nomeArq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(txt)
        except:
            print('Houve um erro na escrita do arquivo!')
        else:
            print(f'Texto adicionado, pronto para ler!')
            a.close()
