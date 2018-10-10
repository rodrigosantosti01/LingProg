# 8 Defna a função junta que recebe como argumentos duas listas de números
# inteiros o1 e o2 e devolve a concatenação de o1 com o2 .
# Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
# Ex: junta([],[4,5,6]) = [4, 5, 6]
# Ex: junta([1,2,3],[]) = [1, 2, 3]



junta = lambda w1,w2: w1+w2


assert(junta([1,2,3],[4,5,6])==[1, 2, 3, 4, 5, 6])
assert(junta([],[4,5,6])==[4,5,6])
assert(junta([1,2,3],[])==[1,2,3])


print(junta([1,2,3],[4,5,6]))
print(junta([],[4,5,6]))
print(junta([1,2,3],[]))


