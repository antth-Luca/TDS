def calc_juros_simples():
    # -- ANOTAÇÕES --
    #  J = juros  (R$ 30,00)
    #  c = capital (R$ 100,00)
    #  i = taxa (10% ao mês)
    #  t = tempo (3 meses)
    #  -- Fórmulas --
    #  1. J = c * i * t
    #  2. c = J / (i * t)
    #  3. i = J / (c * t)
    #  4. t = J / (c * i)

    # -- COLETA --
    print("----- Digite os dados e deixe um campo em branco (apenas aperte 'Enter') para calculá-lo -----")
    J = str(input('Juros (J):\n>> R$ '))
    c = str(input('Capital (c):\n>> R$ '))
    i = str(input('Taxa (i):\n>> '))
    t = str(input('Tempo (n):\n>> '))


    # -- TRATAMENTO --
    #  juros
    if J:
        J = float(J.replace(',', '.'))

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
    if not J:
        print(f'J = R$ {c * i * t}')
    elif not c:
        print(f'c = R$ {J / (i * t)}')
    elif not i:
        print(f'i = {J / (c * t)}% a.m.')
    else:  # elif not t
        print(f't = {J / (c * i)} meses')   


#  MAIN
while(True):
    calc_juros_simples()
    print('=================================================================================')

    respost = ''
    while(not respost):
        respost = str(input('Gostaria de continuar? [S/N] '))
        if respost == '':
            print('Resposta inválida. Tente novamente!')
    
    if respost.upper() == 'N' or respost.upper() == 'NAO' or respost.upper() == 'NÃO':
        break

print('Obrigado por usar um programa de @antthLuca')