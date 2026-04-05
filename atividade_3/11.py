num = int(input("Digite um número: "))
if num % 2 == 0 and num > 0:
    print("Par positivo")
elif num % 2 == 0 and num < 0:
    print("Par negativo")
else:
    print("Ímpar")