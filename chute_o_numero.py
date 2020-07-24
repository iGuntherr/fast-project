import random as rd

n = rd.randrange(100)
j = True

while j:
    v = int(input('Digite um numero de 1 a 100 ou digite 0 para parar: '))
    d = ''

    if v == 0:
        break    
    elif v == n:
        print("You win!!!")
        while True:            
            d = input('Deseja jogar novamente?(s - sim / n não ')
            if d == 's':
                n = rd.randrange(100)
                break
            elif d == 'n':
                j = False
                break
    else:
        t = ('maior' if v > n else 'menor')        
        print(f'Você errou, o número que digitou é *{t}* que o número aletório. Tente novamente.\n')


print('\n###### Obrigado por jogar ######')

    



