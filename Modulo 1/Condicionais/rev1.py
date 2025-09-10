nome = input("Digite o nome do usuário: ")
distancia = int(input("Digite a distância percorrida: "))
combustivel =  int(input("Digite a quantidade de combustível: "))

consumo_medio = distancia/combustivel
if consumo_medio < 8.0:
    print("Consumo médio: ", consumo_medio, "Alto consumo", )
elif consumo_medio >= 8.0 and consumo_medio <= 12.0:
    print("Consumo médio: ", consumo_medio, "Consumo moderado")
elif consumo_medio > 12.0:
    print("Consumo médio: ", consumo_medio, "Econômico!")