agenda = []
while True:
    menu = int(input("Escolha uma das opções: \n [1]Cadastrar pessoa:  \n [2]Listar pessoas:  \n [3]Escluir pessoa:  \n [0]Sair\n"))

    if menu == 1:
        cadastro = input("Insira o nome da pessoa:")
        agenda.append(cadastro)
        print(cadastro)
    elif menu == 2:
        print(agenda)
    elif menu == 3:
        remover =  input("")
        agenda.remove(remover)
    elif menu == 0:
        print("Programa encerrado!")
        break
    else:
        print("Opção Inválida!!!")