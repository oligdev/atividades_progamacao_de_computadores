num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

resto1 = num1 % 3
resto2 = num2 % 3
resto3 = num3 % 3

if resto1 >= resto2 and resto1 >= resto3:
    print(resto1)
    if resto2 >= resto3:
        print(resto2)
        print(resto3)
    else:
        print(resto3)
        print(resto2)
elif resto2 >= resto1 and resto2 >= resto3:
    print(resto2)
    if resto1 >= resto3:
        print(resto1)
        print(resto3)
    else:
        print(resto3)
        print(resto1)
else:
    print(resto3)
    if resto1 >= resto2:
        print(resto1)
        print(resto2)
    else:
        print(resto2)
        print(resto1)