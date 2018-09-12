# 6 Espião: Escreva uma função que receba uma lista de
# inteiros e retorne True se contém um 007 em ordem, mesmo
# que não contínuo. Exemplo:
# espiao([1,2,4,0,0,7,5]) --> True
# espiao([1,0,2,4,0,5,7]) --> True
# espiao([1,7,2,4,0,5,0]) --> False



def espiao(lista):
	status="nada"
	for simbolo in lista:
		if simbolo == 0:
			if status == "nada":
			 	status = "zero"
			elif status == "zero":
				status = "zero zero"
			elif simbolo == 7:
				status = "zero zero sete"
				return status

		


print(espiao([1,2,4,0,0,7,5]))
print(espiao([1,0,2,4,0,5,7]))
print(espiao([1,7,2,4,0,5,0]))