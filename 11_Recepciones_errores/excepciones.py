# def div(a: int, b: int) -> float:
#     if b != 0:
#         return a / b
#
# print(div(1,3))
# print(div(2,0))

#Try-except:
num1 = int(input("ingrese su primer numero: "))
num2 = int(input("ingrese su segundo numero: "))


try:
    print(num1 / num2)
except:
    print("No se ingresaron datos correctos")
