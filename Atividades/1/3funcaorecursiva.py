
def somaFibonacci(n):

    if n == 1: #primeiro termo
        return 0
    elif n == 2: #segundo termo
        return 1
    else:
        return somaFibonacci(n-1) + somaFibonacci(n-2)

print(somaFibonacci(8))#(13
print(somaFibonacci(10))#(34


