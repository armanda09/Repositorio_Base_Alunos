def imprime_padrao(n):
    for i in range(1, n + 1):
        print((str(i) + ' ')* i)

n = int(input("Digite um número inteiro: "))
imprime_padrao(n)