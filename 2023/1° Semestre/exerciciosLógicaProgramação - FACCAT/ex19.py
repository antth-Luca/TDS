contin = True
nums = list()
c = 1
while contin == True:
    nums.append(int(input(f'Digite o {c}° número inteiro a ser analisado: ')))

    if c == 1:
        max = nums[c - 1]
        min = nums[c - 1]
    if nums[c - 1] > max:
        max = nums[c - 1]
    if nums[c - 1] < min:
        min = nums[c - 1]

    while True:
        r = str(input('Você quer continuar? [S/N]\n- ')).strip().capitalize()
        if r == 'N':
            contin = False
            break
        elif r != 'S':
            print('Desculpe, resposta não reconhecida. Tente novamente...')
        else:
            break
    c += 1

if c == 1:
    print('Foi digitado apenas um número...')
elif max == min:
    print('Os numéros digitados são iguais!')
else:
    print(f'O maior número digitado é {max}')
    print(f'O menor número digitado é {min}')
