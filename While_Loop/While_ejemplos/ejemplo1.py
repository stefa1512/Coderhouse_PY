# Bucle While

import math

numero = int(input("Digite un numero: "))

while numero<0:
    print("error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"Su raiz cuadrada es: {(math.sqrt(numero))}")
