def find_proporcao(a, b, c, d):
    equac = {'a': a, 'b': b, 'c': c, 'd': d}
    pos_x = None

    for key, value in equac.items():
        if str(value).upper() == 'X':
            value = 1
            pos_x = key

        equac[key] = int(value)

    # Realizando operação
    passo = [equac['a'] * equac['d'], equac['b'] * equac['c']]
    if pos_x == 'a' or pos_x == 'd':
        result = passo[1] // passo[0]
    else:
        result = passo[0] // passo[1]

    return result


def test_answser():
    assert find_proporcao(16, 4, 8, 'x') == 2
