from function import find_proportion

# Previsão: 0% de cobertura
def test_find1():
    assert find_proportion(16, 4, 8, 'x') == 1 # Incorreto

def test_find2():
    assert find_proportion(16, 4, 'x', 2) == 1 # Incorreto

def test_find3():
    assert find_proportion(9, 3, 3, 'x') == 2 # Incorreto

def test_find4():
    assert find_proportion(0, 'x', 8, 2) == 1 # Incorreto

def test_find5():
    assert find_proportion(16, 4, 0, 'x') == 1 # Incorreto
