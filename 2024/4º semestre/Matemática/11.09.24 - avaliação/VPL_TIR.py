import numpy_financial as npf

TAXA_MINIMA = 0.10  # Exigência mínima de retorno de 10%

# Dados do exercício
fluxos_de_caixa = [30000.00, 35000.00, 40000.00, 45000.00, 50000.00]  # Fluxos de caixa para cada ano
investimento_inicial = 100000.00  # Investimento inicial
taxa_juros = 8  # Taxa de desconto (8%)

# Tratamento de dados
taxa_juros /= 100

# Cálculo do VPL (Valor Presente Líquido)
vpl = sum([fluxo / (1 + taxa_juros) ** (t + 1) for t, fluxo in enumerate(fluxos_de_caixa)]) - investimento_inicial
print(f"VPL: R$ {vpl:.2f}")

# Cálculo da TIR (Taxa Interna de Retorno)
tir = npf.irr([-investimento_inicial] + fluxos_de_caixa) * 100
print(f"TIR: {tir:.2f}%")

# Decisão do projeto
if tir / 100 >= TAXA_MINIMA:
    print("O projeto deve ser aceito.")
else:
    print("O projeto não deve ser aceito.")
