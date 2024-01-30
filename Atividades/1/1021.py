#576.73

#NOTAS:
#5 nota(s) de R$ 100.00
#1 nota(s) de R$ 50.00
#1 nota(s) de R$ 20.00
#0 nota(s) de R$ 10.00
#1 nota(s) de R$ 5.00
#0 nota(s) de R$ 2.00
#MOEDAS:
#1 moeda(s) de R$ 1.00
#1 moeda(s) de R$ 0.50
#0 moeda(s) de R$ 0.25
#2 moeda(s) de R$ 0.10
#0 moeda(s) de R$ 0.05
#3 moeda(s) de R$ 0.01

N = float(input("Informe o Valor: "))

nota100 = N // 100
N = N % 100

nota50 = N // 50
N = N % 50

nota20 = N // 20
N = N % 20

nota10 = N // 10
N = N % 10

nota5 = N // 5
N = N % 5

nota2 = N // 2
N = N % 2 

moeda1 = N // 1
N = N % 1

moeda50 = N // 0.50
N = N % 0.50

moeda25 = N // 0.25
N = N % 0.25

moeda10 = N // 0.10
N =N % 0.10

moeda5 = N // 0.05
N = N % 0.05

moeda01 = round(N / 0.01)


print("NOTAS:")
print(f"{nota100:.0f} nota(s) de R$ 100.00")
print(f"{nota50:.0f} nota(s) de R$ 50.00")
print(f"{nota20:.0f} nota(s) de R$ 20.00")
print(f"{nota10:.0f} nota(s) de R$ 10.00")
print(f"{nota5:.0f} nota(s) de R$ 5.00")
print(f"{nota2:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda1:.0f} moeda(s) de R$ 1.00")
print(f"{moeda50:.0f} moeda(s) de R$ 0.50")
print(f"{moeda25:.0f} moeda(s) de R$ 0.25")
print(f"{moeda10:.0f} moeda(s) de R$ 0.10")
print(f"{moeda5:.0f} moeda(s) de R$ 0.05")
print(f"{moeda01:.0f} moeda(s) de R$ 0.01")
