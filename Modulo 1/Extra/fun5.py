def multiplicar(taxaimposto,custo):
    return custo + ((taxaimposto / 100) * custo)

taxaimposto = float(input("Digite a porcentagem do imposto: "))
custo = int(input("Digite o valor inicial: "))

print("Valor total: ", multiplicar(taxaimposto,custo))