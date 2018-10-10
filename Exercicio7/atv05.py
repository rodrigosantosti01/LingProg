# 5 Defna a função contemnpar que recebe como argumento uma lista de números
# inteiros o e devolve True se o contém um número par e False em caso contrário.
# Ex: contemnpar ([2,3,1,2,3,4]) = True
# Ex: contemnpar ([1,3,5,7]) = False



contemnpar = lambda w: False if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and not contemnpar(w[:-1])) else True

assert(contemnpar([2,3,1,2,3,4]) == True)
assert(contemnpar([1,3,5,7]) == False)

print(contemnpar([2,3,1,2,3,4]))
print(contemnpar([1,3,5,7]))