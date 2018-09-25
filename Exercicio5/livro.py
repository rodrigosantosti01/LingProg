class livro:
	def __init__(self,titulo,numero_pagias,aberto):
		self.titulo = titulo
		self.numero_pagias = numero_pagias
		self.aberto = False
	def abrir(self):
		self.aberto = True
	def fechar(self):
		self.aberto = False

l = livro("Python Como programar",500)