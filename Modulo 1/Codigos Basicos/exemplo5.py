preco_original = int(input("Digite o preco original: "))
porcentagem_desconto = int(input("Digite o valor da porcentagem: "))

valor_desconto = preco_original*(porcentagem_desconto/100)
preco_final = preco_original - valor_desconto
print(preco_final)