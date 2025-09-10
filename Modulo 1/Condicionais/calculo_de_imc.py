nome = input("Nome do paciente: ")
peso = float(input("Peso (kg) do paciente: "))
altura = float(input("Altura (m) do paciente: "))

imc = peso / (altura * altura)
if imc < 18.5:
    print("Nome do paciente: ", nome, "Valor do IMC: ", imc, "Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Nome do paciente: ", nome, "Valor do IMC: ", imc, "Peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print("Nome do paciente: ", nome, "Valor do IMC: ", imc, "Sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
    print("Nome do paciente: ", nome, "Valor do IMC: ", imc, "Obesidade Grau I")
elif imc >= 35.0 and imc <= 39.9:
    print("Nome do paciente: ", nome, "Valor do IMC: ", imc, "Obesidade Grau II")
else:
    print("Nome do paciente: ", nome,  "Valor do IMC: ", imc, "Obesidade Grau III (mórbida)")