'''Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade 
do grupo, qual é o nome do homem mais velho 
e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for pessoa in range(1,5):
    print('====={}ª pessoa======='.format(pessoa).capitalize())
    nome = str(input("Nome:")).strip()
    idade = int(input('idade:'))
    sexo = str(input("[M/F]:")).strip()
    somaidade += idade
    mediaidade = somaidade / pessoa
    if pessoa == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in "fF" and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem,nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

