import random
print("Adivinhe o número sorteado:")
numero_aleatorio = random.randint(1, 101)

for i in range(5):
    adivinhar = int(input(f"{i+1}° tentativa: "))

    if adivinhar == numero_aleatorio:
        print("Você acertou!!🎉 Vamos encerrar o jogo.")
        break
    elif adivinhar < numero_aleatorio:
        diferenca = adivinhar - numero_aleatorio
        if diferenca <= 10:
            print("Quente! Está quase...")
    elif adivinhar > numero_aleatorio:
        diferenca = adivinhar - numero_aleatorio
        if diferenca > 30:
           print("Frio! Tente um valor mais alto.")
    elif adivinhar > 10 and adivinhar <= 30:
        print("Morno.") 
else:
        print(f"Você errou! O número era: {numero_aleatorio}")
    