# 2. Escreva uma função que recebe uma lista de triplas e, para cada uma, gera uma
# equação do segundo grau considerando que os elementos da tripla são os
# coefcientes usualmente denominados a, b e c da equação. Note que a sua função
# deverá devolver uma lista de equações. A geração das equações deve ser feita por
# meio de, evidentemente, decorators.

# 1. Sem usar a notação com @
print("----------------equacoes-------------------------")

def recebe_f(f):
	equacoes = []
	def decorator(lista):
		for e in lista:
			equacoes.append(f(e))
		return equacoes 
	return decorator
def funcao(lista):
	eq = str(lista) + "xˆ2" + "+" + str(lista) + "x" + "+"+ str(lista)
	return eq
funcao = recebe_f(funcao)
print(funcao([2,4,5]))



print("----------------equacoes com @ -------------------------")
# 2. Usando a notação com @, implementando os decorators por meio de funções

def recebe_f2(f2):
	equacoes = []
	def decorator2(lista):
		for e in lista:
			equacoes.append(f2(e))
		return equacoes 
	return decorator2

@recebe_f2
def funcao2(lista):
	eq = str(lista) + "xˆ2" + "+" + str(lista) + "x" + "+"+ str(lista)
	return eq
print(funcao2([7,8,2]))



# 3. Usando a notação com @, implementando os decorators por meio de classes
print("----------------equacoes com @ e classes-------------------------")

class Eq:
	def __init__ (self,f3):
		self.f3 = f3
		self.equacoes =[]
	def __call__(self,lista):
		for e in lista:
			self.equacoes.append(self.f3(e))
		return self.equacoes 
@Eq
def funcao3(lista):
	eq = str(lista) + "xˆ2" + "+" + str(lista) + "x" + "+"+ str(lista)
	return eq
print(funcao3([1,3,2]))


