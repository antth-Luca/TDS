import numpy as np
import pandas as pd
import math

# Carregar os dados do arquivo Excel
df = pd.read_excel('numeros_extracao.xlsx', header=None)

# Flatten the dataframe into a single list of numbers (converter o DataFrame para uma lista)
data = df.values.flatten().tolist()

# Passo 1: Ordenar os dados (ROL)
data_sorted = sorted(data)

# Passo 2: Calcular amplitude total
amplitude_total = max(data_sorted) - min(data_sorted)

# Passo 3: Calcular número de classes (raiz quadrada do número de amostras)
num_classes = math.ceil(np.sqrt(len(data_sorted)))

# Passo 4: Calcular a amplitude de cada classe e ajustá-la para o próximo múltiplo de 6
amplitude_classe = math.ceil(amplitude_total / num_classes)

# Ajustar para ser múltiplo de 6
if amplitude_classe % 6 != 0:
    amplitude_classe += (6 - amplitude_classe % 6)

# Gerar as classes dinâmicas
limite_inferior = min(data_sorted)
limites = [limite_inferior]

while limites[-1] + amplitude_classe <= max(data_sorted):
    limites.append(limites[-1] + amplitude_classe)

# Ajustar o último limite para incluir o maior valor, caso não tenha sido considerado
if limites[-1] < max(data_sorted):
    limites.append(max(data_sorted))

# Definir as classes com base nos limites
classes = [(40, 46), (46, 52), (52, 58), (58,64), (64, 70), (70, 76), (76, 82)]

# Frequências, médias e outras colunas
frequencias = []
limites_inferiores = []
limites_superiores = []

for classe in classes:
    limite_inferior, limite_superior = classe
    
    # Frequência (conta o número de valores que pertencem a essa classe)
    frequencia = sum(limite_inferior <= x < limite_superior for x in data_sorted)
    
    frequencias.append(frequencia)
    limites_inferiores.append(limite_inferior)
    limites_superiores.append(limite_superior)

# Frequência acumulada e porcentagens
frequencias_acumuladas = np.cumsum(frequencias)
porcent_frequencias = [(f / len(data_sorted)) * 100 for f in frequencias]
porcent_frequencias_acumuladas = np.cumsum(porcent_frequencias)

# Tabela final
tabela = {
    'Classes': [f"{cls[0]} |---- {cls[1]}" for cls in classes],
    'Frequência': frequencias,
    'Média': [(cls[1] + cls[0]) / 2 for cls in classes],
    'Frequência Acumulada': frequencias_acumuladas,
    'Porcentagem da Frequência': porcent_frequencias,
    'Porcentagem da Frequência Acumulada': porcent_frequencias_acumuladas
}

df_final = pd.DataFrame(tabela)

# Exibir a tabela
print(df_final)

# Salvar a tabela em um arquivo Excel
df_final.to_excel('tabela_frequencia_dinamica.xlsx', index=False)
