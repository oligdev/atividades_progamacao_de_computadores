try:
    valor = float(input("Digite um valor: "))
    if int(valor) > 10:
        print("Alto")
    else:
        print("Baixo")
except ValueError:
    print("Entrada inválida")