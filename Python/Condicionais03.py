numero = int(input("Digite o número: "))

if numero == 0:
    print("Zero")

elif numero > 0:
    if numero % 2 != 0:
        print("Positivo e Ímpar")
    else:
        print("Positivo e Par")

else:  # aqui significa numero < 0
    if numero % 2 != 0:
        print("Negativo e Ímpar")
    else:
        print("Negativo e Par")