T = int(input("Informe a Quantidade de Casos de Teste: "))

resultados = []

for i in range(T):
    N = int(input("Informe um Número: "))

    if 0 <= N <= 60:   

        a, b = 0, 1

        for j in range(N):

            a, b = b, a + b

        resultados.append((N,a))

for N, resultado in resultados:
            
    print(f"Fib({N}) = {resultado}")
