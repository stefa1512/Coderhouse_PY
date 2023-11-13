ganado = int(input("Cuantos partidos ganaron?: "))
empate = int(input("Cuantos partidos empataron?: "))
perdido = int(input("Cuantos partidos perdieron?: "))

if ganado + empate + perdido >= 20:
    puntaje_prom = (3*ganado + empate)/20
    print(puntaje_prom)
else:
    print("ingresa la cantidad correcta")

