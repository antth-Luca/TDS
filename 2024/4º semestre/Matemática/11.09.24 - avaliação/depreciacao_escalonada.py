def depreciacao_escalonada(valor_inicial, taxas):
    depreciacao_ano = []
    valor_restante = valor_inicial

    for taxa in taxas:
        depreciacao_atual = valor_restante * (taxa / 100)
        depreciacao_ano.append(depreciacao_atual)
        valor_restante -= depreciacao_atual

    return depreciacao_ano, valor_restante

# Dados do problema
valor_inicial = 150000.0  # Valor da máquina em reais
taxas = [40.0, 30.0, 20.0, 10.0, 0.0]  # Porcentagens de depreciação para cada ano

depreciacao, valor_final = depreciacao_escalonada(valor_inicial, taxas)

# Exibir os resultados
for i, valor in enumerate(depreciacao, start=1):
    print(f"Ano {i}: Valor depreciado = R$ {valor:.2f}")

print(f"Valor final após 5 anos: R$ {valor_final:.2f}")
