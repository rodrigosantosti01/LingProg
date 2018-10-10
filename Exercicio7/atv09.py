# 9 Defna a função temPrimo que recebe como argumento uma lista de listas de
# números inteiros o e devolve True se alguma das sublistas o tem um número
# primo e False em caso contrário.
# Ex: temPrimo ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True
# Ex: temPrimo ([[4,4,4,4],[4,4,4],[],[4]]) = False




ehPrimo = lambda p,i=2: False if p==1 else True if p==2 or i>=p else False if p%i==0 and p!=i else ehPrimo(p,i+1)

lista = lambda w: False if len(w)==0 else ehPrimo(w[0]) if len(w)==1 else ehPrimo(w[0]) or lista(w[1:len(w)])

temPrimo = lambda w: False if len(w)==0 else lista(w[0]) if len(w)==1 else lista(w[0]) or temPrimo(w[1:len(w)])


assert(temPrimo([[4,4,4,4],[5,4,6,7],[2,4,3]])==True)
assert(temPrimo([[4,4,4,4],[4,4,4],[],[4]])==False)

print(temPrimo([[4,4,4,4],[5,4,6,7],[2,4,3]]))
print(temPrimo([[4,4,4,4],[4,4,4],[],[4]]))