edad_s = input("Ingrese su edad: ")
antiguedad_s = input("Ingrese su antiguedad: ")
ingresos_s = input("Ingrese su número de ingresos: ")

if edad_s.isnumeric() and antiguedad_s.isnumeric() and ingresos_s.isnumeric():
    edad = int(edad_s)
    antiguedad = int(antiguedad_s)
    ingresos = int(ingresos_s)
    if (edad >= 18) and (antiguedad >= 3 and ingresos >=2500) or (ingresos >= 4000):
        print("Se procede con el prestamo")
    else:
        print("Crédito no aprobado")
else:
    print("Ingrese solo valores numéricos")

