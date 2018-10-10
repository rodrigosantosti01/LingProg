# 7 Defna a função pertence que recebe como argumentos uma lista de números
# inteiros o e um número inteiro n e devolve True se n ocorre em o e False em
# caso contrário.
# Ex: pertence ([1,2,3],1) = True
# Ex: pertence ([1,2,3],2) = True
# Ex: pertence ([1,2,3],3) = True
# Ex: pertence ([1,2,3],4) = False

pertence = lambda w,n: True if n in w else False



assert(pertence([1,2,3],1) == True)
assert(pertence([1,2,3],2) == True)
assert(pertence([1,2,3],3) == True)
assert(pertence([1,2,3],4) == False)

print(pertence([1,2,3],1))
print(pertence([1,2,3],2))
print(pertence([1,2,3],3))
print(pertence([1,2,3],4))
