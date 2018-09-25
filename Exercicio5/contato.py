class Contato:
	def __init__(self,nome,numero):
		self.nome=nome
		self.numero=numero
	

def cadastro_de_contatos():
	menu= '1-cadastrar\n 2-Listar \n0-Sait\n'
	op = int(input(menu))
	while op !=0:
		if op ==1:
			file = open("agenda.txt","a")
			try:
				nome = input("Digite o Nome")
				numero = input("Digite o Numero")
				file.write(nome + ";" + numero + "\n")
				file.close()
			except IOError:
				print("Nao Deu Certo")
			finally:
				print("print passou por aqui")
		elif op ==2:
			try:
				contatos=[]
				with open ("agenda.txt", "r") as outro_file:
					linhas = outro_file.readlines()
					for linha in linhas: 
						partes = linha.split(";")
						contato = Contato(partes[0],partes[1])
						contatos.append(contato)
				for contato in contatos:
					print(contato)
			except IOError:
				pass
			finally:
				print("Finally Passando")

		else:
			print("Tchau")
		op = int(input(menu))
cadastro_de_contatos()
