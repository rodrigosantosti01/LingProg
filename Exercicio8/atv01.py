# 1. Escreva uma função que calcula a soma dos n primeiros números naturais, dado
# que n é recebido como parâmetro. Escreva um decorator que garanta que o valor
# recebido é natural (maior ou igual a 1).



# 1. Sem usar a notação com @
print("----------------valida -------------------------")
def valida (f):
	def soma_n_primeiros(n):
		if (n>=1):
			return f(n)		
		else:
			print("Numero menor que 1")
			return 0
	return soma_n_primeiros
def outra_funcao(n):
	soma=0
	for x in range(n+1):
		soma = soma + x
	return soma

outra_funcao = valida(outra_funcao)
print(outra_funcao(4))
print(outra_funcao(0))


print("----------------valida com @ -------------------------")
# 2. Usando a notação com @, implementando os decorators por meio de funções

def valida2 (f2):
	def soma_n_primeiros2(n):
		if (n>=1):
			return f2(n)		
		else:
			print("Numero menor que 1")
			return 0
	return soma_n_primeiros2

@valida2
def outra_funcao2(n):
	soma=0
	for x in range(n+1):
		soma = soma + x
	return soma

print(outra_funcao2(3))
print(outra_funcao2(0))

# 3. Usando a notação com @, implementando os decorators por meio de classes


print("----------------valida com @  e classes-------------------------")


class Validar:
	def __init__(self,f3):
		self.f3 = f3
	def __call__(self,n):
		if (n>=1):
			return self.f3(n)		
		else:
			print("Numero menor que 1")
			return 0
@Validar
def outra_funcao2(n):
	soma=0
	for x in range(n+1):
		soma = soma + x
	return soma

print(outra_funcao2(5))
print(outra_funcao2(0))

