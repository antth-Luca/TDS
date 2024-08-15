from math import log

def format_taxa(i):
    i = i.upper()

    if 'A.A.' in i or 'A.A' in i or 'AA.' in i or 'AA' in i:
        i = i.upper().replace('A.A.', '').replace('A.A', '').replace('AA.', '').replace('AA', '')
        dividir = 12
    elif 'A.D.' in i or 'A.D' in i or 'AD.' in i or 'AD' in i:
        i = i.upper().replace('A.D.', '').replace('A.D', '').replace('AD.', '').replace('AD', '')
        dividir = 30
    else: # 'A.M.' in i or 'A.M' in i or 'AM.' in i or 'AM' in i
        dividir = 1

    porcent = False
    if '%' in i:
        i = i.replace('%', '')
        porcent = True

    i = float(i.replace(',', '.'))

    if porcent:
        i /= 100
    i /= dividir

    return i

def format_tempo(t):
    if t.upper()[-1] == 'A' or 'ANOS' in t.upper() or 'ANO' in t.upper():
        t = t.upper().replace('ANOS', '').replace('ANO', '').replace('A', '')
        t = float(t) / 12
    elif 'D' in t.upper() or 'DIAS' in t.upper() or 'DIA' in t.upper():
        t = t.upper().replace('DIAS', '').replace('DIA', '').replace('D', '')
        t = float(t) / 30
    else:  # 'M' in t.upper() or 'MESES' in t.upper() or 'MÊS' in t.upper() or 'MES' in t.upper()
        t = t.upper().replace('MESES', '').replace('MÊS', '').replace('MES', '').replace('M', '')
        t = float(t)

    return t

def calc_taxa_dcd():
    # -- ANOTAÇÕES --
    #  Va = valor atual (R$ 72,90)
    #  Vn = valor nominal composto (R$ 100,00)
    #  i = taxa (10% ao mês)
    #  t = tempo (3 meses)
    #  -- Fórmulas --
    #  1. i = 1 - (Va / Vn)^(1 / t)

    # -- COLETA --
    print("----- Digite os dados e deixe um campo em branco (apenas aperte 'Enter') para calculá-lo -----")
    Vn = str(input('Valor nominal (VN):\n>> R$ '))
    Va = str(input('Valor atual (VA):\n>> R$ '))
    t = str(input('Tempo (n):\n>> '))


    # -- TRATAMENTO --
    #  valor nominal
    if Vn:
        Vn = float(Vn.replace(',', '.'))

    # valor atual
    if Va:
        Va = float(Va.replace(',', '.'))

    #  tempo
    if t:
        t = format_tempo(t)


    # -- OPERAÇÕES --
    print(f'i = {1 - pow((Va / Vn), (1 / t)):.3f}')

def calc_periodo():
    # -- ANOTAÇÕES --
    #  Va = valor atual (R$ 700,00)
    #  Vn = valor nominal composto (R$ 900,00)
    #  i = taxa (4,9% ao mês)
    #  t = tempo (5 meses)
    #  -- Fórmulas --
    #  1. (logVA - logVN) / log(1 - i)

    # -- COLETA --
    print("----- Digite os dados e deixe um campo em branco (apenas aperte 'Enter') para calculá-lo -----")
    Vn = str(input('Valor nominal (VN):\n>> R$ '))
    Va = str(input('Valor atual (VA):\n>> R$ '))
    i = str(input('Taxa (i):\n>> '))


    # -- TRATAMENTO --
    #  valor nominal
    if Vn:
        Vn = float(Vn.replace(',', '.'))

    # valor atual
    if Va:
        Va = float(Va.replace(',', '.'))

    #  taxa
    if i:
        i = format_taxa(i)


    # -- OPERAÇÕES --
    print(f'n = {(log(Va) - log(Vn)) / log(1 - i):.3f}')


# MAIN
calc_periodo()
