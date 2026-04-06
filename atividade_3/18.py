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