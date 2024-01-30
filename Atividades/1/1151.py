N = int(input("Informe um Valor: "))

vetor = [0]*N

for i in range(0, N):

    if i <= 1:
        vetor[i] = i
    else:
        vetor[i] = vetor[i-1] + vetor[i-2]
    
    if i == N - 1:
        print("%d"%(vetor[i]), end="")
    else:
        print("%d"%(vetor[i]),end=" ")

print()