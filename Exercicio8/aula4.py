import time

def cria_decorator_time(funcao):
	def decora():
		t0 = time.time()
		funcao()
		return time.time()-t0
	return decora

@cria_decorator_time
def funcao_demorada():
	for i in range(10):
		print(i)
		time.sleep(1)


print(funcao_demorada.__name__)