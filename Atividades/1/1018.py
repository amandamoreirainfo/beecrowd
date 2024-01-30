
N = int(input("Informe o Valor: "))

print(N)

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

nota1 = N // 1

print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")
