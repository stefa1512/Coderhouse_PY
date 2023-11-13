# def suma(num1: int, num2: int):
#     total = num1 + num2
#     return total
#
# def resta(num1: int, num2: int):
#     total2 = num1 -num2
#     return total2
#
# print(f"El total de la suma es: {suma(num2=2, num1=5)}")
# print(f"El total de la suma es: {resta(num2=2, num1=5)}")
#


# #default
# def resta_default(num1: int = 2, num2: int = 0):
#     total2 = num1 -num2
#     return total2
#
#
# print(f"El total de la suma es: {resta_default(num1=5, num2=2)}")
# print(f"El total de la suma es: {resta_default(num1=5)}")
# print(f"El total de la suma es: {resta_default()}")
#
#

# #MODIFICAR VALOR
# def modify(value):
#     value = value*2
#     return value
#
# value_start = ("lUIS","cARLOS")
# value_modify = modify(value_start)
# print(value_start)
# print(value_modify)

#  #Modificar por referencia
# def doblar(numeros):
#     for i, n in enumerate(numeros):  # i: índices (0,1,2) - n: (10, 50 ,100)
#         numeros[i] *= 2
#
# lis_n = [10, 50, 100]
# print(lis_n)
# doblar(lis_n)
# print(lis_n)

# #*args -> listas
# def suma(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(f"El total de la suma es {suma(*[2, 5, 2, 45, 5 ,6 ,32])}")
#
#
# #**kwargs -> diccionarios
# def suma(**kwargs):
#     total = 0
#     for key, num in kwargs.items():
#         print(f"Sumando la referencia {key}: {num}")
#         total += num
#     return total
# print(f"El total de la suma es {suma(num1 = 2, num2 = 5, num3 = 45, num4 = 2)}")

# args y kwargs - mostrar los valores con refencia y sin referencia 
def suma(*args, **kwargs):
    """
    Esta función resive...
    """
    print(args)
    print(kwargs)
    total = 0
    for key, num in kwargs.items():
        print(f"Sumando la referencia {key}: {num}")
        total += num
    return total
print(f"El total de la suma es {suma( 1 ,2 ,3 , [' dadasda', 'asdasd'], num1 = 2, num2 = 5, num3 = 45, num4 = 2)}")

