# 8 Defna a função junta que recebe como argumentos duas listas de números
# inteiros w1 e w2 e devolve a concatenação de w1 com w2 .
# Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
# Ex: junta([],[4,5,6]) = [4, 5, 6]
# Ex: junta([1,2,3],[]) = [1, 2, 3]


def junta(w1,w2):
   return w1+w2


print(junta([1,2,3],[4,5,6]))
print(junta([],[4,5,6]))
print(junta([1,2,3],[]))

