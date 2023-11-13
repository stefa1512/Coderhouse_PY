#age = int(input("Ingresa tu edad: "))

#while age < 1:
   # print("No ingresaste una edad válida")
   # age = int(input("Ingresa tu edad: "))

#print(f"Tienes {age} años")


num = int(input("Ingresa un número 1 a 10: "))
while num < 1 or num > 10:
    print("El número no es válido")
    num = int(input("Ingresa un número 1 a 10: "))

print(f"Tu número es {num}")



