num = int(input("Digite um número inteiro: "))
if num % 5 == 0:
    if num > 50:
        print("Múltiplo alto")
    else:
        print("Múltiplo baixo")
else:
    print("Não é múltiplo")