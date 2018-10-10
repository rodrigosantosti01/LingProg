# 4 Defna a função prodnlista que recebe como argumento uma lista de inteiros e
# devolve o produto dos seus elementos.
# Ex: prodnlista([1,2,3,4,5,6]) = 720


prodnlista = lambda lista: lista[len(lista) - 1] * prodnlista(lista[:-1]) if len(lista) > 0 else 1

assert(prodnlista([1,2,3,4,5,6]) == 720)
assert(prodnlista([2,2,2]) == 8)

print(prodnlista([1,2,3,4,5,6]))
print(prodnlista([2,2,2]))