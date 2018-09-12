#  Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver
# em alguma posição da lista um 3 do lado de outro 3. Exemplo:
# tem_33([1,3,3]) --> True
# tem_33([1,3,1,3]) --> False
# tem_33([3,1,3]) --> False


def tem_33(lista):
	status="nada"
	for simbolo in lista:
		if simbolo == 3:
			if status == "nada":
			 	status = "Tres"
			elif status == "Tres":
				return True
		else:
			if status == "Tres":
				status = "nada"
	return False

print(tem_33([3,3,1]))
print(tem_33([3,1,3,1,3,1]))
print(tem_33([1,1,1,3,3,1,1,1,3]))

