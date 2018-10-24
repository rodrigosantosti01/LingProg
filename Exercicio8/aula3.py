def cria_decorator(funcao):	
	def decorator() :
		print( 'testando..',mensagem)
		funcao()
	return decorator
@cria_decorator
def funcao_a_ser_decorada():
	print("testa")
	
funcao_a_ser_decorada()