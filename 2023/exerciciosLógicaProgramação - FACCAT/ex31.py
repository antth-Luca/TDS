print('\033[33m{}{}{}\033[m'.format('=-' * 10, 'Triângulos', '-=' * 10))
a = float(input('Digite o valor, \033[31mem metros\033[m, da primeira reta: '))
b = float(input('Digite o valor, \033[31mem metros\033[m, da segunda reta: '))
c = float(input('Digite o valor, \033[31mem metros\033[m, da terceira reta: '))
if a > abs(b - c) and a < (b + c) and b > abs(a - c) and b < (a + c) and c > abs(a - b) and c < (a + b):
    print('As retas podem formar um triângulo', end=' ')
    if a == b == c == a:
        print('\033[32mEQUILÁTERO\033[m!')
    elif a == b and a != c or b == c and b != a or c == a and c != b:
        print('\033[32mISÓCELES\033[m!')
    elif a != b != c != a:
        print('\033[32mESCALENO\033[m!')
else:
    print('As retas \033[35mnão\033[m podem formar um triângulo.')
print('\033[33m=-\033[m' * 25)