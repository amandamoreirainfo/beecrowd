

def soma(vetor):

    if not vetor: # se não for vetor retorna 0
        return 0
    else:
        return vetor[0:] + soma(vetor[1:])
        #Ele inicia no indice 1 e vai até o final do vetor.


print(soma([1,2,3,10]))#16
print(soma([-1,18,-16,2,0,13,4]))#20
