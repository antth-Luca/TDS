from time import sleep

comprando = True
morangos = 0
macas = 0


print(50 * '-=')
print('{:^100}'.format('Frutaria Frutíssima'))
print(50 * '-=')

print('Compras iniciadas!', end=' ')
while True:
    r = str(input('Você quer adicionar MORANGOS ou MAÇÃS à sua sacola? [S/N]\n- ')).strip().upper()
    if r == 'N':
        print('Encerrando...')
        exit()
    elif r != 'S':
        print('Opção inválida. Tente novamente...')
    else:
        break
while comprando:
    while True:
        if r == 'N':
            break
        f = str(input('Qual fruta você quer? [MO-morangos/MA-maçãs]\n- ')).strip().upper()
        if f != 'MO' and f != 'MA':
            print('Não entendi, por favor, tente novamente.')
        else:
            kg = float(input('Ótimo! De quantos quilos você precisa?\n- '))
            if f == 'MO':
                morangos += kg
            else:
                macas += kg
        while True:
            r = str(input('Você quer adicionar mais alguma coisa na sua sacola? [S/N]\n- ')).strip().upper()
            if r == 'N':
                comprando = False
                break
            elif r == 'S':
                break
            else:
                print('Ops! Acho que não entendi, vamos tentar mais uma vez...')
if morangos <= 5:
    vMO = morangos * 2.5
else:
    vMO = morangos * 2.2
if macas <= 5:
    vMA = macas * 1.8
else:
    vMA = macas * 1.5
print('''\nNa sua sacola existem...
{}Kg de morangos..........R${:.2f}
{}Kg de maças.............R${:.2f}
__________________________________
Soma......................R${:.2f}'''.format(morangos, vMO, macas, vMA, vMO + vMA))
sleep(0.5)
if morangos + macas > 8 or vMO + vMA > 25:
    print(
        '\nPara clientes Frutíssimo existe uma condição especial, onde se sua compra ultrapassar 8Kg de frutas ou o '
        'valor total passar de R$25,00\nvocê ganha um incrível desconto!')
    print(f'R${vMO + vMA:.2f} - 10% de desconto'
          f'\nValor final= R${(vMO + vMA) - ((vMO + vMA) * 0.1):.2f}')
