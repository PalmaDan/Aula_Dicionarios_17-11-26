# Ex3 Dicionário vazio, 1.adicionar:
#nome: "Telemóvel"
#preço: 1500
#stock: 30
#2. Remove a chave stock do dinheiro
#3. Imprime o dic final

produto = {}

produto["nome"] = "Telemóvel"
produto["preço"] = 1500
produto["stock"] = 30

produto.pop("stock")

print(produto)