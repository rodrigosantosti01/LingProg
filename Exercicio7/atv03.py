# 3 Defna a função primnalg que recebe como argumento um número natural e
# devolve o primeiro algarismo (o mais signifcatvo) na representação decimal de n.
# Ex: primnalg(5649) = 5
# Ex: primnalg(7) = 7


primnalg = lambda numero: numero if numero<10 else primnalg(numero//10)

assert(primnalg(5649) == 5)
assert(primnalg(7) == 7)


print(primnalg(5649))
print(primnalg(7))