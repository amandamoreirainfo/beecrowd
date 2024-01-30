
#25
#100
#5.50

#NUMBER = 25
#SALARY = U$ 550.00

numeroFuncionario = int(input("Informe o número do Funcionário: "))
horasTrabalhadas = int(input(f"Informe o número de Horas Trabalhadas: "))
valorPorHora = float(input("Informe o Valor que Recebe por Hora: "))

salarioFuncionario = horasTrabalhadas * valorPorHora

print(f"NUMBER = {numeroFuncionario}")
print(F"SALARY = U${salarioFuncionario: .2f}")