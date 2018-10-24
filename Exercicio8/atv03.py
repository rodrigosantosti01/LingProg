# 3. Escreva uma função que exibe uma lista recebida como parâmetro. Ela deve,
# contudo, ordenar a lista antes. A ordenação deve ser feita por meio de um
# decorator.





# 1. Sem usar a notação com @
print("----------------ordenada-------------------------")

def ordena(f):
	def decorator(lista):
		return f(sorted(lista))
	return decorator

def funcao(lista):
	print(lista)

funcao = ordena(funcao)
print(funcao([3,1,5,2,0,10,4,6]))



print("----------------ordenada com @ -------------------------")
# 2. Usando a notação com @, implementando os decorators por meio de funções

def ordena2(f2):
	def decorator(lista):
		return f2(sorted(lista))
	return decorator

@ordena2
def funcao2(lista):
	print(lista)

print(funcao2([11,0,1,2,4,10,3,6]))


# 3. Usando a notação com @, implementando os decorators por meio de classes
print("---------------- ordenada com @ e classes-------------------------")

class Ordena:
	def __init__ (self,f3):
		self.f3 = f3
	def __call__(self,lista):
		return self.f3(sorted(lista))
@Ordena
def funcao3(lista):
	print(lista)
print(funcao3([30,0,5,2,1,100,4,20]))




