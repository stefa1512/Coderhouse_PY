def factoria(num):
    if num == 1:
        return 1
    return num*factoria(num - 1)
print(factoria(10))



# 1 1 2 3 5 8 13
def fibo(n):
    if n == 1 or n ==2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(25))

