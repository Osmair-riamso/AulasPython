'''Faça um programa que leia o peso de cinco
pessoas. No final, mostre qual foi o maior
e o menor peso lidos.  '''

pesomaior = 0
pesomenor = 0

for p in range (1,6):
    peso = float(input("Digite o peso da {}ª pessoa:".format(p)))
    if p == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:        
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
            
print('O maior peso lido foi de {}Kg.'.format(pesomaior))
print('O menor peso lido foi de {}Kg.'.format(pesomenor))
