nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário do produto: R$ "))
quantidade = int(input("Digite a quantidade do produto: "))

preco_total = preco_unitario * quantidade

print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", preco_total)