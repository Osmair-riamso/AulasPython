from time import sleep

primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o segundo valor: "))
escolha = 0
while escolha != 5:
    print('''        [1] Somar
        [2] Multiplicar
        [3] Qual o maior Número
        [4] Digitar novos numeros
        [5] Sair do programa''')
    escolha = int(input("\nO que voce deseja fazer com os numeros {} e {}? ".format(primeiroValor,segundoValor)))
    if escolha == 1:
        soma = primeiroValor + segundoValor
        print("A soma de {} e {} é {}.".format(primeiroValor,segundoValor,soma))
    elif escolha == 2:
        multiplicao = primeiroValor * segundoValor
        print("A multiplicao de {} e {} é {}.".format(primeiroValor,segundoValor,multiplicao))
    elif escolha == 3:
        if primeiroValor > segundoValor:
            maior = primeiroValor
        else:
            maior = segundoValor
        print("O Maior numero entre {} e {} é {}.".format(primeiroValor,segundoValor,maior))    
    elif escolha == 4:
        print(" Deseja mudar os numeros?")
        primeiroValor = int(input("Digite o primeiro numero: "))
        segundoValor = int(input("Digite o segundo numero: "))
    elif escolha == 5:
        
        print("Finalizando....")
        print("+=="*10)
        sleep (3)
    else:
        print("Opção invalida!!!")
   
print("Até mais!")
        
