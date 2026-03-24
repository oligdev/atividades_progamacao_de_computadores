#Algoritmo que calcula salário total de um funcionário  
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))
salario_total = horas_trabalhadas * valor_hora
print("O salário total é: R$ {:.2f}".format(salario_total))

