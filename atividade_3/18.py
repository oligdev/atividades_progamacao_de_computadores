# Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro.
num = int(input("Digite um número: "))
if num == 0:
    print("Neutro")
elif num % 2 == 0:
    if num > 0:
        print("Par positivo")
    else:
        print("Par negativo")
else:
    if num > 0:
        print("Ímpar positivo")
    else:
        print("Ímpar negativo")