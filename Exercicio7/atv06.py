# 6 Defna a função todosnimpares que recebe como argumento uma lista de
# números inteiros o e devolve True se o contém apenas números ímpares e False
# em caso contrário.
# Ex: todosnimpares ([1,3,5,7]) = True
# Ex: todosnimpares ([]) = True
# Ex: todosnimpares ([1,2,3,4,5]) = False



todosnimpares = lambda w: True if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and todosnimpares(w[:-1])) else False

assert(todosnimpares([1,3,5,7]) == True)
assert(todosnimpares([]) == True)
assert(todosnimpares([1,2,3,4,5]) == False)


print(todosnimpares([1,3,5,7]))
print(todosnimpares([]))
print(todosnimpares([1,2,3,4,5]))