

N =  int(input("Informe o número: "))
V = list(map(int, input().split()))
posicao = 0
menor = V[0]
count = 0


for i in V:

    if i < menor:

        menor = i
        posicao = count
    
    count +=1

    V.append(N)

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
