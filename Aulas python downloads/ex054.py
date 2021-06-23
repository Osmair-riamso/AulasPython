'''Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas ainda 
não atingiram a maioridade e quantas já são maiores. '''

from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range (1,8):
    anoNascimento = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(pessoa)))
    idade =  atual - anoNascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
        
print('\nTemos um total de {} pessoas maiores de idade'.format(totmaior))
print('\nTemos um total de {} pessoas menores de idade'.format(totmenor))