
def  sequencia(T):
    
    N = [0]*100 
    for i in range(100):

        N[i] = i%T

    return N

  

T = int(input("Informe um Valor: "))
V = sequencia(T)

for j in range(len(V)):
    print(f"N[{j}] = {V[j]}")



