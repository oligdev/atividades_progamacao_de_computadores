#Algoritmo para calcular IMC
print("Bem-vindo ao calculador de IMC!")
nome = input("Digite seu nome: ")
print("Olá, {}!".format(nome) + " Este programa irá calcular o seu Índice de Massa Corporal (IMC).")
peso = float(input("{}, digite seu peso em kg: ".format(nome)))
altura = float(input("{}, digite sua altura em metros: ".format(nome)))
imc = peso / (altura ** 2)
print("{}, seu IMC é: {:.2f}".format(nome, imc))
if imc < 18.5:
    print("{}, você está abaixo do peso.".format(nome))
elif imc < 25:
    print("{}, você está com peso normal.".format(nome))
elif imc < 30:
    print("{}, você está com sobrepeso.".format(nome))
else:
    print("{}, você está com obesidade.".format(nome))
