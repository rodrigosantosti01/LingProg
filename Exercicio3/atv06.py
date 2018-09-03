# 6. Faça um Programa que leia um número e exiba o dia
# correspondente da semana. (1-Domingo, 2- Segunda, etc.), se
# digitar outro valor deve aparecer valor inválido.



dia_semana = int(input("Digite um numero de 1 a 7: "))

if(dia_semana == 1):
	print("voce digitou %s - Domingo" %(dia_semana))
elif(dia_semana==2):
	print("voce digitou %s - Segunda" %(dia_semana))
elif(dia_semana==3):
	print("voce digitou %s - Terça" %(dia_semana))
elif(dia_semana==4):
	print("voce digitou %s - Quarta" %(dia_semana))
elif(dia_semana==5):
	print("voce digitou %s - Quinta" %(dia_semana))
elif(dia_semana==6):
	print("voce digitou %s - Sexta " %(dia_semana))
elif(dia_semana==7):
	print("voce digitou %s - Sabado " %(dia_semana))
else:
	print("numero inválido %s" %(dia_semana))