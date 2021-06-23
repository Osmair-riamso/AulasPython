'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores 
e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou 
não continuar a digitar valores. '''
cond = "S"
soma = cont = media = 0

while cond in 'SN':
    n = int(input("Digite um numero: "))    
    soma += n
    
    
    cond =str(input("Deseja continuar? S/N ")).strip()[0].upper()
    
print("FIM")

