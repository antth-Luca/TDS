import math

def find_delta(a, b, c):
    return pow(b, 2) - (4 * a * c)


def find_x(a, b, delta):
    if delta == 0:
        return (b * -1) / (2 * a)
    elif delta > 0:
        return [((b * -1) + math.sqrt(delta)) / (2 * a), ((b * -1) - math.sqrt(delta)) / (2 * a)]
    else:
        return None


def baskara(a, b, c):
    result = find_x(a, b, find_delta(a, b, c))

    print('O valor', end=' ')
    if isinstance(result, float):
        print(f'de x é {result}!')
    elif result and len(result) == 2:
        print(f'de x1 é {result[0]} e de x2 é {result[1]}!')
    else:
        print('de x não existe!')


baskara(2, -4, 2)  # Delta igual a 0
baskara(1, -5, 6)  # Delta maior que 0
baskara(1, 4, 5)  # Delta menor que 0