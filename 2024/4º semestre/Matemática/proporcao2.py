import re

def get_operador(expressao):
    # Procurar por operadores +, -, *, ou /
    match = re.search(r'[\+\-\*/]', expressao)
    if match:
        return match.group()
    else:
        return None


equac = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
pos_x = None
expressao = {'operador': None, 'valor': {'x': None, 'operação': None}}
chuveiro = None
passo = None

# Obtendo dados
for key in equac:
    digit = str(input(f'Digite o número {key}:\n>> '))

    # Tratando expressões com X
    if 'X' in digit.upper():
        expressao['operador'] = get_operador(digit)
        terciario = digit.split(expressao['operador'])

        if terciario[0].upper() == 'X':
            expressao['valor']['x'] = 1
        else:
            expressao['valor']['x'] = int(terciario[0][:-1])

        expressao['valor']['operação'] = int(terciario[1])

        equac[key] = 1
        pos_x = key
    else:
        equac[key] = int(digit)

    print('\n')

# -- OPERAÇÕES --
# Chuveiro/Distribuição
if pos_x == 'a':
    chuveiro = [equac['b'] * equac['c'], equac['d'] * expressao['valor']['x'], equac['d'] * expressao['valor']['operação']]
elif pos_x == 'b':
    pass
elif pos_x == 'c':
    pass
else:  # pos_x == 'd'
    pass

# Operando expressão
if expressao['operador'] == '+':
    passo = chuveiro[0] - chuveiro[2]

# Cálculo do resultado e apresentação do mesmo
print(passo // chuveiro[1])
