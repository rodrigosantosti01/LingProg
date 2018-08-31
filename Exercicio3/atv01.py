# 1. Faça um Programa que peça dois números e imprima o maior
# deles.


numero_um = int(input("digite um numero: "))	
numero_dois = int(input("digite outro numero: "))

if(numero_um>numero_dois):
	print("o numero 1 é o maior: %s" %(numero_um))
elif(numero_um==numero_dois):
	print("Ambos numeros são iguais: numero 1: %s e numero 2: %s" %(numero_um,numero_dois))
elif(numero_um<numero_dois):
	print("o numero 2 é o maior: %s" %(numero_dois))