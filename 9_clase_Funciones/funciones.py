# #Def estandar:
# def saludar_a_los_estudiantes():
#     print("hola como estan")
#
# saludar_a_los_estudiantes()
#
# #Def con parámetro:
# def saludar_estudiantes(nombre):
#     print(f"Hola como estas: {nombre}")
# saludar_estudiantes("Stefano")
#
# #Def con retorno:
# def retornar_saludo_a_estudiantes(nombre):
#     #Esta funcion retornara un string con el saludo del estudiante que se le ingreso
#     mensaje = f"Hola como estar {nombre}"
#     return mensaje
# print(retornar_saludo_a_estudiantes("Stefano D'Alfonso"))
#
#
# def test():
#     var_test = 10
#     print(var_test)
# test()
#
#
# def test2(numero):
#     signo = f"El valor es {numero}"
#     return signo
# print(test2(10))
#
#
# def suma(numero1, numero2):
#     total = numero1 + numero2
#     mensaje = f"El resultado de la suma es {total}"
#     return mensaje
#
# num1 = int(input("Ingrese el primer numero a sumar"))
# num2 = int(input("Ingrese el segundo numero a sumar"))
# print(suma(num1, num2))


def pais(lugar):
    place = f"Hola, bienvenido a: {lugar}"
    return place
saludo = input("Ingrese el nombre del país: ")
print(pais(saludo))


def muestra_lista():
    for i in lis:suma = 0

