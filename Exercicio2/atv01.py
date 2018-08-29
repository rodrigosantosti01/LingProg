# Atividade 01 -  
# Crie um programa que recebe uma lista de números e
# - retorne o maior elemento
# - retorne a soma dos elementos
# - retorne o número de ocorrências do primeiro elemento da lista
# - retorne a média dos elementos
# - retorne o valor mais próximo da média dos elementos
# - retorne a soma dos elementos com valor negativo
# - retorne a quantidade de vizinhos iguais



lista = []
count = 0
negativos = 0
while count < 5 :
	numeros = int(input("Digite um numero: "))
	lista.append(numeros)
	count +=1
print (lista)
print (max(lista))
print (sum(lista))
print (lista.count(lista[0]))
print (int(sum(lista)/len(lista)))
media = (int(sum(lista)/len(lista)))
print("media",media)


maisProximo = lista[0]
dmp = media - lista[0]
menorDiferenca = dmp

for i in lista:
	dmp = media - i
	if(dmp == 0):
		maisProximo = i
	if(dmp < 0):
		dmp = dmp *-1
	if(dmp<menorDiferenca):
		menorDiferenca = dmp
		maisProximo = i 

print("numero mais proximo: %s " %(maisProximo))

for i in lista:
	if i<0 :
		negativos += i
print ("numeros negativos: %s " %(negativos))



	
