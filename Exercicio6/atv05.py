# 5 Defina a função contemnparQ que recebe como argumento uma lista de números
# inteiros w e devolve True se w contém um número par e False em caso contrário.


# Ex: contemnparQ([2,3,1,2,3,4]) = True
# Ex: contemnparQ([1,3,5,7]) = False


contem_parQ = lambda w: False if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and not contem_parQ(w[:-1])) else True

assert(contem_parQ([2,3,1,2,3,4]) == True)
assert(contem_parQ([1,3,5,7]) == False)

print(contem_parQ([2,3,1,2,3,4]))
print(contem_parQ([1,3,5,7]))