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

def calc_valor_nominal():
    # -- ANOTAÇÕES --
    #  VNcc = valor nominal composto (R$ 100,00)
    #  VA = valor atual (R$ 72,90)
    #  i = taxa (10% ao mês)
    #  t = tempo (3 meses)
    #  -- Fórmulas --
    #  1. VNcc = VA / (1 - i)^n

    # -- COLETA --
    print("----- Digite os dados e deixe um campo em branco (apenas aperte 'Enter') para calculá-lo -----")
    Va = str(input('Valor atual (VA):\n>> R$ '))
    i = str(input('Taxa (i):\n>> '))
    t = str(input('Tempo (n):\n>> '))


    # -- TRATAMENTO --
    #  valor atual
    if Va:
        Va = float(Va.replace(',', '.'))

    #  taxa
    if i:
        i = format_taxa(i)


    #  tempo
    if t:
        t = format_tempo(t)


    # -- OPERAÇÕES --
    print(f'VNcc = R$ {Va / pow((1 - i), t):.2f}')

def calc_valor_desconto():
    # -- ANOTAÇÕES --
    #  Dcc = desconto composto (R$ 27,10)
    #  VN = valor nominal composto (R$ 100,00)
    #  i = taxa (10% ao mês)
    #  t = tempo (3 meses)
    #  -- Fórmulas --
    #  1. Dcc = VN * [1 - (1 - i)^t]

    # -- COLETA --
    print("----- Digite os dados e deixe um campo em branco (apenas aperte 'Enter') para calculá-lo -----")
    Vn = str(input('Valor nominal (VN):\n>> R$ '))
    i = str(input('Taxa (i):\n>> '))
    t = str(input('Tempo (n):\n>> '))


    # -- TRATAMENTO --
    #  valor nominal
    if Vn:
        Vn = float(Vn.replace(',', '.'))

    #  taxa
    if i:
        i = format_taxa(i)

    #  tempo
    if t:
        t = format_tempo(t)


    # -- OPERAÇÕES --
    print(f'Dcc = R$ {Vn * (1 - pow((1 - i), t))}')

# MAIN
calc_valor_desconto()
