
def soma(n):

    if n  == 0: 
        return 0
    else:#Se n não for igual a zero, a função retorna a soma de n com a chamada recursiva, sendo responsável por calcular a soma dos números anteriores a n.
        return n + soma(n-1)

print(soma(3))#(3+2+1) = 6 - calcula a soma dos primeiros 3 números inteiros
print(soma(6))#(6+4+5+3+2+1) = 21 - calcula a soma dos primeiros 6 números inteiros
