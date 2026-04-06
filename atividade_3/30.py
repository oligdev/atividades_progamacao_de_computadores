valor = input("Digite um valor: ")
try:
    num = int(valor)
    if num % 2 == 0:
        if num > 100:
            print("Par alto")
        else:
            print("Par baixo")
    else:
        print("Ímpar")
except ValueError:
    print("Entrada inválida")