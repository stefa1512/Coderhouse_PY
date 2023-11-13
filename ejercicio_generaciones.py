year_s = input("Ingrese un año: ")
if year_s.isnumeric():
	year = int(year_s)
	if 1920 <= year <= 1940 :
		print("Generacion Silenciosa")
	elif 1941 <= year <= 1964:
		print("Baby Boomer")
	elif 1965 <= year <= 1979:
		print("Generacion X")
	elif 1980 <= year <= 2000:
		print("Generacion Y")
	elif 2001 <= year <= 2010:
		print("Generacion Z")
	else:
		print("No tienes una generación definida")
else:
	print("Ingrese un año")
