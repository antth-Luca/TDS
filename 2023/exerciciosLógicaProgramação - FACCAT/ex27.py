n = int(input('Digite um número inteiro para analisar: '))
print(f'O número {n} é', end=' ')
if n == 0:
    print('Zero.')
elif n > 0:
    print('Positivo!')
else:
    print('Negativo!')
