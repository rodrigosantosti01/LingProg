# 9 Defna a função temPrimoQ que recebe como argumento uma lista de listas de
# números inteiros w e devolve True se alguma das sublistas w tem um número
# primo e False em caso contrário.
# Ex: temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True
# Ex: temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False

def ehPrimo(p,i=2):	
	if p==1:
		return False
	if p==2 or i>=p:
		return True
	if p%i==0 and p!=i:
		return False
	return ehPrimo(p,i+1) 

def lista(w):
	if (len(w)==0):
		return False
	else:
		if(len(w)==1):
			return ehPrimo(w[0])
		else:
			return ehPrimo(w[0]) or lista(w[1:len(w)])

def temPrimoQ(w):
	if (len(w)==0):
		return False
	else:
		if(len(w)==1):
			return lista(w[0])
		else:
			return lista(w[0]) or temPrimoQ(w[1:len(w)])


print(temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]))
print(temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]))

