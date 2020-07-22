import random as rd

n = int(input('Digite 1 para rodar os dados ou 0 para parar: '))

while n == 1:
    seq = [*range(1,21)]
    print(f'O lado do dado é: {rd.choices(seq)}')
    n = 5
    while n != 1 and n != 0:
        n = int(input('Digite 1 para rodar os dados ou 0 para parar: '))

print('###### Fim de jogo ######')