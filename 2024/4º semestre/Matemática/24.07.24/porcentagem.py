def porcentagem(valor: int, porcent:int):
    print(f'- {porcent}% de {valor} = {(valor // 100) * porcent}')


# MAIN
porcentagem(20000, 6)
porcentagem(20000, 10)
porcentagem(75000, 6)
porcentagem(100000, 7)
