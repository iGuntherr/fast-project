import random as rd

n = int(input('Digite 1 para rodar os dados ou 0 para parar: '))
d = 0
lados = [4, 6, 8, 10, 12, 20]

while n == 1:

    if d in lados:
        while True:
            msg = input('Deseja trocar de dado? (s / n) ')
            if msg == 's':
                d = 0
                break
            elif msg == 'n':
                break 

    while d not in lados:
        d = int(input(f'Quantos lados terá seu dado? Opções {lados} '))  

    
    seq = [*range(1,d + 1)]
    print(f'O lado do dado é: {rd.choices(seq)}')
    n = 5
    while n != 1 and n != 0:
        n = int(input('Digite 1 para rodar os dados ou 0 para parar: '))

print('\n###### Fim de jogo ######')