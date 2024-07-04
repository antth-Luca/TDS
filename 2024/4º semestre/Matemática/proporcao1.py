equac = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
pos_x = None

# Obtendo dados
for key in equac:
    digit = input(f'Digite o número {key}:\n>> ')

    if digit.upper() == 'X':
        digit = 1
        pos_x = key

    equac[key] = int(digit)
    print('\n')

# Realizando operação
passo = [equac['a'] * equac['d'], equac['b'] * equac['c']]
if pos_x == 'a' or pos_x == 'd':
    result = passo[1] // passo[0]
else:
    result = passo[0] // passo[1]

print(result)
