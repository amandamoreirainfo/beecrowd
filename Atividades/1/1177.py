T = int(input("Informe um Valor: "))
N = [0]*1000 

for i in range(1000):

    N[i] = i%T

for j in range(len(N)):
    print(f"N[{j}] = {N[j]}")



