# Atividade - 3 

# Faça um programa que receba duas listas e retorne True se têm
# os mesmos elementos ou False caso contrário
# Duas listas possuem os mesmos elementos quando são compostas
# pelos mesmos valores, mas não obrigatoriamente na mesma ordem.



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
lista.sort()
lista2.sort()
print (lista==lista2)