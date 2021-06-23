''' Melhore o DESAFIO 61, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa
encerrará quando ele disser que quer mostrar 0 termos.  '''
from time import sleep
print("Gerador de PA")
print("+="*12)

n1 = int(input("digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = n1
cont = 1
total =0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print ('{} → '.format(termo),end ='' )
        termo += razao
        cont += 1
    print ('PAUSA')
    mais = int(input('''
                     Quantos termos voce quer mostrar mais? 
                     Digite 0 para encerrar.'''))
print("Finalizando programa >>>>")
sleep(1)
print("Programa finalizado com {} termos solicitados.".format(total))



