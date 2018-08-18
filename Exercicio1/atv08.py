# Atividade 8 
# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# - salário bruto.
# - quanto pagou ao INSS.
# - quanto pagou ao sindicato.
# - o salário líquido.
# - calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%8 : R$
# - INSS (8%8 : R$
# - Sindicato ( 5%8 : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


salario_hora  = float(input("Quanto você ganha por hora: "))
numero_horas_trabalhadas = float(input("Quantas horas você trabalha durante o mês: "))

total_salario = salario_hora*numero_horas_trabalhadas
print ("salário bruto R$: %s" %(total_salario))

ir = total_salario*(11/100)
print ("quanto pagou de IR R$: %s" %(ir))

inss = total_salario*(8/100)
print ("quanto pagou ao Inss R$: %s" %(inss))

sindicato = total_salario*(5/100)
print ("quanto pagou ao Sindicato R$: %s" %(sindicato))

descontos = ir+inss+sindicato

total_salario_liquido=total_salario - descontos
print ("Salário Liquido R$: %s" %(total_salario_liquido))
