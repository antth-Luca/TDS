from time import sleep

c = 0
while True:
    tipo_combust = str(input('Qual o combustível abastecido? [G-gasolina/A-álcool]\n- ')).strip().upper()
    if tipo_combust != 'G' and tipo_combust != 'A':
        print('Houve um erro de digitação. Tente mais uma vez...')
    else:
        break
    if c == 2:
        print('Desisto da humanidade!')
        exit()
    c += 1

l = float(input('Quantos litros foram abastecidos?\n- '))
print(30 * '-=')
print(f'{"Calculando...":^60}')
print(30 * '-=')
sleep(1)

if tipo_combust == 'G':
    tipo_combust = 'gasolina'
    if l <= 20:
        t = l * (3.3 - (3.3 * 0.03))
    else:
        t = l * (3.3 - (3.3 * 0.05))

elif tipo_combust == 'A':
    tipo_combust = 'álcool'
    if l <= 20:
        t = l * (2.9 - (2.9 * 0.04))
    else:
        t = l * (2.9 - (2.9 * 0.06))

print(f'Por {l}L de {tipo_combust} o cliente pagará R${t:.2f}')
