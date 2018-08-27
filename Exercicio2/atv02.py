# Atividade 2 
# Faça um programa que receba duas listas e retorne True se são
# iguais ou False caso contrario.
# Duas listas são iguais se possuem os mesmos valores e na mesma
# ordem.

lista=[]
lista2=[]
count=0
while count < 3 :
	numeros = int(input("Insira na primeira lista: "))
	numeros2 = int(input("Insira na segunda lista: "))
	lista.append(numeros)
	lista2.append(numeros2)
	count +=1
print (lista,lista2)
print(lista==lista2)

