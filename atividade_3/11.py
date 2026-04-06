#Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”.
num = int(input("Digite um número: "))
if num % 2 == 0 and num > 0:
    print("Par positivo")
elif num % 2 == 0 and num < 0:
    print("Par negativo")
else:
    print("Ímpar")
