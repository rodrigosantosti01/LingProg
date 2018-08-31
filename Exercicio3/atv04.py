# 4. Faça um Programa que leia três números e mostre-os em ordem
# decrescente.

contador =0
lista = []


while contador< 3:
	numero = int(input("Digite a segunda nota: "))
	contador +=1 
	lista.append(numero)

listaReversa = sorted(lista,reverse=True)
print(listaReversa)
for numeros in listaReversa:
	print (numeros)