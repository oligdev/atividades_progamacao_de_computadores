num = int(input("Digite um número inteiro: "))
if num > 0:
    if num % 2 == 0 and num % 3 == 0:
        print("Múltiplo de 2 e 3")
    else:
        print("Não atende")
else:
    print("Número inválido")