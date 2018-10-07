# 10 Defna a função inverteLista que recebe como argumento uma lista w e devolve a
# mesma lista mas invertda.
# Ex: inverteLista([1,2,3,4,5]) = [5, 4, 3, 2, 1]
# Ex: inverteLista([])


def inverteLista(w):
	return w[::-1]

print(inverteLista([1,2,3,4,5]))
print(inverteLista([]))