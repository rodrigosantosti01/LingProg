# Atividade - 3 
# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês.



horas_trabalhadas=0
dinheiro_hora = 0.0
print("Digite o valor R$ recebido por hora de trabalho")
dinheiro_hora = float(input())
print("Digite quantidade de horas trabalhadas durante o mês")
horas_trabalhadas = int(input())

total = horas_trabalhadas*dinheiro_hora
print("O total do seu salário mensal é: R$ %s" %(total))