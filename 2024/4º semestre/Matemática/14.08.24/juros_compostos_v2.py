from math import log

def calc_juros_compostos():
    # -- ANOTAÇÕES --
    #  M = montante  (R$ 133,10)
    #  c = capital (R$ 100,00)
    #  i = taxa (10% ao mês)
    #  t = tempo (3 meses)
    #  -- Fórmulas --
    #  1. i = [(M / C)^(1/t)] - 1
    # ex1. 0.10 ao mês = [(133,10 / 100)^(1/3 meses)] - 1
    #  2. n = (logM - logC) / log(1 + i)
    # ex2. 3 meses = (log133,10 - log100) / log(1 + 0,10 ao mês)

    # -- COLETA --
    print("----- Digite os dados e deixe um campo em branco (apenas aperte 'Enter') para calculá-lo -----")
    M = str(input('Montante (M):\n>> R$ '))
    c = str(input('Capital (c):\n>> R$ '))
    i = str(input('Taxa (i):\n>> '))
    t = str(input('Tempo (n):\n>> '))


    # -- TRATAMENTO --
    #  montante
    if M:
        M = float(M.replace(',', '.'))

    #  capital
    if c:
        c = float(c.replace(',', '.'))

    #  taxa
    if i:
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


    #  tempo
    if t:
        if t.upper()[-1] == 'A' or 'ANOS' in t.upper() or 'ANO' in t.upper():
            t = t.upper().replace('ANOS', '').replace('ANO', '').replace('A', '')
            t = float(t) / 12
        elif 'D' in t.upper() or 'DIAS' in t.upper() or 'DIA' in t.upper():
            t = t.upper().replace('DIAS', '').replace('DIA', '').replace('D', '')
            t = float(t) / 30
        else:  # 'M' in t.upper() or 'MESES' in t.upper() or 'MÊS' in t.upper() or 'MES' in t.upper()
            t = t.upper().replace('MESES', '').replace('MÊS', '').replace('MES', '').replace('M', '')
            t = float(t)


    # -- OPERAÇÕES --
    if not i:
        print(f'i = {(pow((M / c), (1 / t)) - 1):.3f}')
    elif not t:
        print(f'n = {(log(M) - log(c)) / log(1 + i):.2f}')


# MAIN
calc_juros_compostos()
