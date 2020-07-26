import random as rd

resposta = ['Nem que a vaca tussa', 'Sim, pode ter certeza!', 'Nem a pau', 'Positivo, é isso mesmo!', 'Não!! De jeito nenhum!', 'Sempre soube, aproveita!!', 'Ta na cara que vai dar ruim', 'Sim! Vai lá', 'Habsulutamente não', 'Experimenta! Aproveita e chama o crush!']

while True:
    n = rd.randrange(len(resposta))
    perg = input('Faça uma pergunta de sim ou não ou digite 0 para parar: ')
    if perg == '0':
        break
       
    print(resposta[n])