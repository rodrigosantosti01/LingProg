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
while count < 2 :
	numeros = int(input("Digite um numero: "))
	lista.append(numeros)
	count +=1
print (lista)
print (max(lista))
print (sum(lista))
print (lista.count(lista[0]))
print (int(sum(lista)/len(lista)))
print (float(sum(lista)/len(lista)))

for i in lista:
	if i<0 :
		negativos += i
print (negativos)


quantidade_numeros_iguais = 0
for j in lista:
	aux = j
	
