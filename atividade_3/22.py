'''Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro. Caso não seja
possível realizar a conversão, exiba: “Entrada inválida”. Caso a conversão seja bem-sucedida: Se
o número for maior que 10, exiba: “Alto”. Caso contrário, exiba: “Baixo”.'''
try:
    valor = float(input("Digite um valor: "))
    if int(valor) > 10:
        print("Alto")
    else:
        print("Baixo")
except ValueError:
    print("Entrada inválida")