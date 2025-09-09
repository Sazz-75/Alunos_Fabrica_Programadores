# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 09/09/2025

# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR

#Samuel victor alves dias  


print("                                                  ")
print("Bem vindo a calculadora de indice de massa corporal  ")
print("                                                  ")


n1 = float(input("digite seu peso: "))
n2 = float(input("digite sua altura: "))


def calculo (n1, n2):
    return n1 /(n2 * n2)

imc = calculo (n1, n2)

print(f"seu indice de massa corporal é {imc}")

if imc <= 18.5:
    print("" \
    "abaixo do peso: \n" \
    "Volte sempre ")

elif imc <= 24.9:
    print("" \
    "Voce esta com peso normal\n" \
    "volte sempre ")

elif imc <= 29.9:
    print("" \
    "sobrepeso: " \
    "volte sempre")

elif imc <= 34.9:
    print("" \
    "obesidade gral 1: " \
    "volte sempre ")

elif imc <= 39.9:
    print("" \
    "obesidade grau 2: " \
    "volte sempre ")

else:
    print("" \
    "obesidade grau 3 cuidado: " \
    "obrigado volte sempre ")








































