produto1 = int(input("Digite o valor do primeiro produto: "))
produto2 = int(input("Digite o valor do segundo produto: "))
produto3 = int(input("Digite o valor do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("Produto mais barato: ", produto1)
if produto2 < produto1 and produto2 < produto3:
    print("Produto mais barato: ", produto2)
if produto3 < produto1 and produto3 < produto2:
    print("Produto mais barato: ", produto3)