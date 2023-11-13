edad = input("Ingrese su edad: ")
antiguedad = input("Ingrese su tiempo en el sistema financiero: ")
ingresos = input("Ingrese total de ingresos: ")

if edad.isnumeric() and antiguedad.isnumeric() and ingresos.isnumeric():
    edad = int(edad)
    antiguedad = int(antiguedad)
    ingresos = int(ingresos)
    if edad >= 18 and ((antiguedad >= 3 and ingresos >= 2500) or ingresos >= 4000):
        print("Credito aprobado")
    else:
        print('Credito no aprobado')
