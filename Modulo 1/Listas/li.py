lista = [1,2,3,4,5]
for i in range(1,11):#1 numero a mais
    print(i) #i variavel temporarea

for batata in lista:#for na lista é para repetir a funçao e mudar o valor
    print(batata)#interar dentro da lista

print (lista)#copia tudo

lista1 = ["camisa","blusa", "meia", "saia", "boné"]
for i in lista1:#demonstraçao de produtos
    print("--------")
    print(f"O produto é: {i}")
    print("--------")
lista1.append("sapato")#adiciona no final da lista
print(lista1)

lista1.insert(0, "bota")#coloca o elemento na posiçao que vc quer
print(lista1)

lista1[0] = "cueca"#alterou(trocou) o valor da bota pela cueca 
print(lista1)

del lista1[0]#deleta
print(lista1)

lista1.remove("camisa")#so remove a primeira ocorrencia do valor na lista
print(lista1)

lista1.pop(2)#pop remove e apresenta o que foi removido
print(lista1)

lista1.clear()
print(lista1)

numeros = [1,2,3,4]
for numero in numeros:
    print(numero)

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for letra in letras:
    print(letra)