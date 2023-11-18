from lib.interface import *
import pyttsx3

#Preparando a voz que fará a leitura
voz = pyttsx3.init()

#Instruções para usar função open()
#"r" - Leitura - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir
#"a" - Anexar - Abre um arquivo para anexar, cria o arquivo se ele não existir
#"w" - Write - Abre um arquivo para escrita, cria o arquivo se ele não existir
#"x" - Create - Cria o arquivo especificado, retorna um erro se o arquivo existir
#Além disso, você pode especificar se o arquivo deve ser tratado como modo binário ou texto
#"t" - Texto - Valor padrão. modo de texto
#"b" - Binário - Modo binário (por exemplo, imagens)


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


def chamar(nome):
    txt = 1000 * (nome + ', ')
    cont = True
    cabeçalho('Sendo insistente...')
    voz.say(txt)
    voz.runAndWait()


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
