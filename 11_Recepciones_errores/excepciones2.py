num1 = 5
num2 = 3

try:
    f = open("dDadadas")
    f.write(32)
    div = num1 / num2
    div_0 = div / 0

except (ZeroDivisionError,TypeError) as err:  #se pueden juntar las excepciones considerando los parametros de respuesta, si tienen distintos parámetros se coloca otro except
    print(err)

else:
    print("no se generaron excepciones")  #se puede colocar aqui o en el final del try

finally:
    f.close()
    print("Se ejecuto despues del erro o sin error")  #Se ejecuta siempre con o sin error, sirve para cerrar el código.

print("todo salio bien")
