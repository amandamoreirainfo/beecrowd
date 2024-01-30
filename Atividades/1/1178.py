X = float(input("Informe um Valor: "))
N = [] 

for i in range(100):

    N.append(X)
    X = X / 2
            
    print('N[{0}] = {1:.4f}'.format(i,N[i]))
    #Formatar Strings permite que voce substitua valores em uma string em locais específicos.




