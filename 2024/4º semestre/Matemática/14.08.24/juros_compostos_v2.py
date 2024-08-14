def calc_taxa_juros_compostos():
    # -- ANOTAÇÕES --
    #  M = montante  (R$ 133,10)
    #  c = capital (R$ 1000,00)
    #  i = taxa (10% ao mês)
    #  t = tempo (3 meses)
    #  -- Fórmulas --
    #  1. i = [(M / C)^(1/t)] - 1

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
        print(f'i = R$ {(pow((M / c), (1 / t)) - 1):.2f}')


# MAIN
calc_taxa_juros_compostos()
