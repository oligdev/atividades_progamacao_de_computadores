valor = input("Digite um valor: ")
try:
    num = int(valor)
    print(f"Dobro: {num * 2}")
except ValueError:
    try:
        num = float(valor)
        print(f"Metade: {num / 2}")
    except ValueError:
        print("Tipo inválido")