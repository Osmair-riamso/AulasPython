'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while. '''
print("Gerador de PA")
print("+="*12)

n1 = int(input("digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = n1
cont = 1

while cont <= 10:
    print ('{} → '.format(termo),end ='' )
    termo += razao
    cont += 1
print ('Fim')
    