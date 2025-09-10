while True:
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if nome != senha:
        break
    print("Senha inválida! Digite novamente.")