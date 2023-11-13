
num1 = input("numero 1: ")
num2 = input("numero 2: ")

try:
    def dividir(a: int, b: int) -> float:
        if b > 0:
            return a/b
    print(dividir(num1, num2))

except TypeError:
    print("No se puede dividir entre cero")

print("todo en orden")
