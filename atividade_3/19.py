num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 == num2:
    print("Os números são iguais.")
else:
    print(f"Os números são diferentes. A diferença entre eles é: {abs(num1 - num2)}")