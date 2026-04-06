num = int(input("Digite um número inteiro: "))
if num > 0:
    if num < 10:
        print("Pequeno")
    elif num <= 100:
        print("Médio")
    else:
        print("Grande")
else:
    print("Negativo ou zero")