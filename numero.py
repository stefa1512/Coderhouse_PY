edad_s = input("Ingrese su edad: ")
if edad_s.isnumeric():
	edad = int(edad_s)
	if edad >= 18:
		print("Es mayor de edad")
	elif edad >=13:
		print("Es adolescente")
	elif edad >=5:
		print("Es un niño")
	elif edad >=0:
		print("Es un bebe")
	else:
		print("La edad ingresada es incorrecta")
else:
	print("La edad debe ser un número")

if edad == 34: print("Es un profe")

mensaje= "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
