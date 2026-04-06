num = int(input("Digite um número inteiro: "))
if 1 <= num <= 100:
    if num % 2 == 0:
        print("Par no intervalo")
    else:
        print("Ímpar no intervalo")
else:
    print("Fora do intervalo")