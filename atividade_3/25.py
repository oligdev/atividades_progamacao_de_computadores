valor = input("Digite um valor: ")
print(f"Tipo: {type(valor)}")
try:
    num = float(valor)
    print(f"Resultado da divisão por 2: {num / 2}")
except ValueError:
    print("Não numérico")