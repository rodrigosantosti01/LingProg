
def cria_hello_decorator(funcao):
	def hello_decorator():
		print ("antes")
		funcao()
		print("depois")
	return hello_decorator

def hello_decorators():
	print ("hello,decorators")

hello_decorators = cria_hello_decorator(hello_decorators)
hello_decorators()



