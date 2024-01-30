
#JOAO
#500.00
#1230.30

#TOTAL = R$ 684.54

nomeVendedor = input("Informe o Nome do Vendedor: ")
salarioFixo = float(input(f"Informe o Salário Fixo do {nomeVendedor}: "))
totalVendasPorMes = float(input("Informe o Total de Vendas por Mês: "))
comissao = 0.15

totalReceberFinalMes = salarioFixo + (comissao * totalVendasPorMes)

print(f"TOTAL = R${totalReceberFinalMes: .2f}")
