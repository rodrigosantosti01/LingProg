class Pessoa:
	contador = 0 
	def __init__(self,nome,idade):
		self.nome = nome
		self.idade = idade
		Pessoa.contador +=1

print(Pessoa.contador)
p1 = Pessoa("Ana",21)
print(Pessoa.contador)
p2 = Pessoa("Jose",34)
print(Pessoa.contador)

print (f'p1:{p1.nome},{p1.idade}')
print (f'p1:{p2.nome},{p2.idade}')
