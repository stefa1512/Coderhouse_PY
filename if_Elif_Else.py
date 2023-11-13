edad_s = input("Ingrese un numero: ")
if edad_s.isnumeric():
    edad = int(edad_s)
    if edad >= 18:
	    print("Es un adulto")
    elif edad >= 0:
	    print("Es menor de edad")
    else:
	    print("La edad ingresada es incorrecta")
else:
    print("La edad debe ser un numero")

if edad == 34: print("Es el profe")
mensaje = "Es mayor de edad" if edad >= 18 else "es menor de edad"
print(mensaje)
