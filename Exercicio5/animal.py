class Animal:
	def __init__(self,nome):
		self.nome = nome
		print("Animal saindo da jaula")
	def quemSouEu(self):
		print("animal")

	def __str__(self):
		return f'Animal:{self.nome}'
	def __len__(self):
		return len(self.nome)

	def __del__(self):
		print (f"{self.nome} sendo apagado")

class Dog(Animal):
	
	def __init__(self):
		super(Animal, self).__init__()
	
	def quemSouEu(self):
		print("Dog 2")


a = Animal("Cachorro")
print(a)

# a.quemSouEu()



# b = Dog()
# b.quemSouEu()
