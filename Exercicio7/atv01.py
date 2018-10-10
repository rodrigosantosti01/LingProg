# 1 Defna a função somannat que recebe como argumento um número natural n
#  e devolve a soma de todos os números naturais até n.
# Ex: somannat(5) = 15


somannat = lambda n: 1 if n==1 else n + somannat(n-1)

assert(somannat(5) == 15)
print(somannat(5))