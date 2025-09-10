def converter_dolar_real(valor):
    return valor * 5.59

def converter_dolar_real2(valor):
    return valor / 5.59

converter = input("[Digite -> 1] -  Converter Dólar para Real:\n[Digite -> 2] - Conveter Real para Dólar: \n")
valor = input("Digite o valor a ser convertido: ")

try:
    converter = float(converter)
    valor = float(valor)

    if converter == 1:
        print(converter_dolar_real(valor))

    elif converter == 2:
        print(converter_dolar_real2(valor))

except:
    print("Digite um valor correto")