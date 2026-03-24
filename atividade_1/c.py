#Algoritmo calcular o reajuste com imposto em um produto
preco = float(input("Digite o preço do produto: "))
reajuste = float(input("Digite o percentual de reajuste (em %): "))
imposto = float(input("Digite o percentual de imposto (em %): "))
preco_reajustado = preco + (preco * reajuste / 100)
preco_final = preco_reajustado + (preco_reajustado * imposto / 100)
print(f"O preço final do produto após o reajuste e o imposto é: {preco_final:.2f}")
