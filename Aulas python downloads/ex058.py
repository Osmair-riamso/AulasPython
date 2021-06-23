'''Melhore o jogo do DESAFIO 28 onde o computador vai
“pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint

computador = randint(0,10)

print('<<<< Jogo de adivinhação >>>>')

acertou = False
palpites = 0
while not acertou:
    print("Que numero estou pensando de 0 a 10 ? ")
    jogador = int(input("Digite um numero: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("É menos, tente novamente!\n")
        elif jogador < computador:
            print("É mais, tente novamente!\n")
print("Voce tentou {} vezes, parabens o numero era {} voce acertou!".format(palpites,computador))

