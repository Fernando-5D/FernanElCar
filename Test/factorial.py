def Factorial(n):
    factorial = 1
    for x in range(1, n + 1):
        factorial *= x
    
    return factorial

num = int(input("Numero = "))
print(str(Factorial(num)))