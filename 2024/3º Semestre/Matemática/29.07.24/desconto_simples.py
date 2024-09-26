# Dcs (Desconto Comercial Simples) = VN * i * n
# Drs (Desconto Racional Simples) = (VN * i * n) / (1 + (i * n))

# VN = Valor nominal (R$ 100,00)
# i = Taxa ao mês (10% => 0,10)
# n = Tempo em meses (3 meses)

# Dcs = R$ 23,08
# Drs = R$ 30,00

def desconto_comercial_simples():
    VN = str(input('Valor nominal (VN):\n>> R$ '))
    i = str(input('Taxa (i):\n>> '))
    t = str(input('Tempo (n):\n>> '))

    # -- TRATAMENTO --
    #  juros
    if VN:
        VN = float(VN.replace(',', '.'))

    #  taxa
    if i:
        if '%' in i:
            i = i.replace('%', '')
        if 'A.A.' in i.upper() or 'A.A' in i.upper() or 'AA.' in i.upper() or 'AA' in i.upper():
            i = i.upper().replace('A.A.', '').replace('A.A', '').replace('AA.', '').replace('AA', '')
            i = (float(i) / 100) / 12
        elif 'A.D.' in i.upper() or 'A.D' in i.upper() or 'AD.' in i.upper() or 'AD' in i.upper():
            i = i.upper().replace('A.D.', '').replace('A.D', '').replace('AD.', '').replace('AD', '')
            i = (float(i) / 100) / 30
        else:  # 'A.M.' in i.upper() or 'A.M' in i.upper() or 'AM.' in i.upper() or 'AM' in i.upper()
            i = i.upper().replace('A.M.', '').replace('A.M', '').replace('AM.', '').replace('AM', '')
            i = float(i) / 100

    #  tempo
    if t:
        if t.upper() == 'A' or 'ANOS' in t.upper() or 'ANO' in t.upper():
            t = t.upper().replace('ANOS', '').replace('ANO', '').replace('A', '')
            t = float(t) / 12
        elif 'D' in t.upper() or 'DIAS' in t.upper() or 'DIA' in t.upper():
            t = t.upper().replace('DIAS', '').replace('DIA', '').replace('D', '')
            t = float(t) / 30
        else:  # 'M' in t.upper() or 'MESES' in t.upper() or 'MÊS' in t.upper() or 'MES' in t.upper()
            t = t.upper().replace('MESES', '').replace('MÊS', '').replace('MES', '').replace('M', '')
            t = float(t)

    # -- OPERAÇÕES --
    print(f'O desconto comercial simples é R$ {float(VN * i * t)}')
    print('=================================================================================')


def desconto_racional_simples():
    VN = str(input('Valor nominal (VN):\n>> R$ '))
    i = str(input('Taxa (i):\n>> '))
    t = str(input('Tempo (n):\n>> '))

    # -- TRATAMENTO --
    #  juros
    if VN:
        VN = float(VN.replace(',', '.'))

    #  taxa
    if i:
        if '%' in i:
            i = i.replace('%', '')
        if 'A.A.' in i.upper() or 'A.A' in i.upper() or 'AA.' in i.upper() or 'AA' in i.upper():
            i = i.upper().replace('A.A.', '').replace('A.A', '').replace('AA.', '').replace('AA', '')
            i = (float(i) / 100) / 12
        elif 'A.D.' in i.upper() or 'A.D' in i.upper() or 'AD.' in i.upper() or 'AD' in i.upper():
            i = i.upper().replace('A.D.', '').replace('A.D', '').replace('AD.', '').replace('AD', '')
            i = (float(i) / 100) / 30
        else:  # 'A.M.' in i.upper() or 'A.M' in i.upper() or 'AM.' in i.upper() or 'AM' in i.upper()
            i = i.upper().replace('A.M.', '').replace('A.M', '').replace('AM.', '').replace('AM', '')
            i = float(i) / 100

    #  tempo
    if t:
        if t.upper() == 'A' or 'ANOS' in t.upper() or 'ANO' in t.upper():
            t = t.upper().replace('ANOS', '').replace('ANO', '').replace('A', '')
            t = float(t) / 12
        elif  'DIAS' in t.upper() or 'DIA' in t.upper() or 'D' in t.upper():
            t = t.upper().replace('DIAS', '').replace('DIA', '').replace('D', '')
            t = float(t) / 30
        else:  # 'M' in t.upper() or 'MESES' in t.upper() or 'MÊS' in t.upper() or 'MES' in t.upper()
            t = t.upper().replace('MESES', '').replace('MÊS', '').replace('MES', '').replace('M', '')
            t = float(t)

    # -- OPERAÇÕES --
    print(f'O desconto comercial simples é R$ {float((VN * i * t) / (1 + (i * t)))}')
    print('=================================================================================')


# MAIN
desconto_racional_simples()
