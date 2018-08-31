# 5. As Organizações Tabajara resolveram dar um aumento de salário
# aos seus colaboradores e lhe contrataram para desenvolver o
# programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5% Após o
# aumento ser realizado, informe na tela:
# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - o valor do aumento;
# - o novo salário, após o aumento.



salario_colaborador = float(input("digite o salário do colaborador: "))

if (salario_colaborador<=280.00):
	valor_reajuste = salario_colaborador * (20/100)
	salario_colaborador = salario_colaborador + valor_reajuste
	print(salario_colaborador)
	print("o salário sofreu um reajuste de 20%% passou a ser %s" %(salario_colaborador))

elif(salario_colaborador>280.00 and salario_colaborador < 700.00):
	valor_reajuste = salario_colaborador * (15/100)
	salario_colaborador = salario_colaborador + valor_reajuste
	print(salario_colaborador)
	print("o salário sofreu um reajuste de 15%% passou a ser %s" %(salario_colaborador))

elif(salario_colaborador>= 700.00 and salario_colaborador < 1500.00):
	valor_reajuste = salario_colaborador * (10/100)
	salario_colaborador = salario_colaborador + valor_reajuste
	print(salario_colaborador)
	print("o salário sofreu um reajuste de 10%% passou a ser %s" %(salario_colaborador))

elif(salario_colaborador> 1500.00):
	valor_reajuste = salario_colaborador * (5/100)
	salario_colaborador = salario_colaborador + valor_reajuste
	print(salario_colaborador)
	print("o salário sofreu um reajuste de 5%% passou a ser %s" %(salario_colaborador))