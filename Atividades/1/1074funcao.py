
def parOuImpar(X):
    
    entradas = []
    for i in range(X):

        N = int(input("Informe o Valor: "))
        entradas.append(N)

    saidas = []

    for N in entradas:

        if N == 0:
            print("NULL")
        elif N % 2 == 0 and N > 0:
            print("EVEN POSITIVE")
        elif N % 2 == 0 and N < 0:
            print("EVEN NEGATIVE")
        elif N % 2 != 0 and N > 0:
            print("ODD POSITIVE")
        elif N % 2 != 0 and N < 0:
            print("ODD NEGATIVE")
        
    for saida in saidas:
        print(saida)

X = int(input("Informe o Número de Casos de Teste: "))
parOuImpar(X)

