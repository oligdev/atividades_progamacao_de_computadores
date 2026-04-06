#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado.
valor = input("Digite um valor: ")
print(f"Tipo: {type(valor)}")
try:
    num = float(valor)
    print(f"Quadrado: {num ** 2}")
except ValueError:
    print("Não é numérico")
