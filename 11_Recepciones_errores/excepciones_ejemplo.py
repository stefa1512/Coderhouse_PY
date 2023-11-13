while True:
    num1 = input("numero 1: ")
    num2 = input("numero 2: ")

    try:
        num1 = int(num1)
        num2 = int(num2)
        div = num1/num2
        break
    except ValueError:
        print("no ingreso un numero valido, intentemoslo de nuevo")
    except ZeroDivisionError:
        print("no ingreso un numero valido, intentemoslo de nuevo")

print("todo en orden")
