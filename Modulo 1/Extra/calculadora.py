num1 = input("Digite o 1º número: ")
num2 = input("Digite o 2º número: ")

try:
    opção = float(input("Escolha uma operação: soma (+)\n subtração (-)\n multiplicação (*)\n divisão (/)\n"))
    if opção == "+":
        print(f"O valor da soma é: {num1 + num2}")
    elif opção == "-":
        print(f"O valor da soma é: {num1 - num2}")
    elif opção == "*":
        print(f"O valor da soma é: {num1 * num2}")
    elif opção == "/":
        print(f"O valor da soma é: {num1 / num2}")

except:
    print("Digite um valor correto!")