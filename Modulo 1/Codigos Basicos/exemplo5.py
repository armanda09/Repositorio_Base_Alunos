valor_desconto=int(input("digite o valor do desconto"))
preco_original=int(input("digite o valor original"))
preco_final=int(input("digite o preco final"))

valor_desconto=preco_original *(20/100)
preco_final=preco_original-valor_desconto
print(preco_final)