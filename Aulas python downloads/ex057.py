'''Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja 
errado, peça a digitação novamente até ter um valor
correto.'''

sexo = str(input("digite seu sexo: [M/F]")).strip().upper()[0]

while sexo not in "mMfF":
    sexo = str(input("Dados invalidos. Por favor Digite usando M ou F ")).strip() .upper()[0]
   
print("Sexo {} registrado com sucesso".format(sexo))

