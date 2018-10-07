# 7 Defna a função pertenceQ que recebe como argumentos uma lista de números
# inteiros w e um número inteiro n e devolve True se n ocorre em w e False em
# caso contrário.
# Ex: pertenceQ([1,2,3],1) = True
# Ex: pertenceQ([1,2,3],2) = True
# Ex: pertenceQ([1,2,3],3) = True
# Ex: pertenceQ([1,2,3],4) = False



def pertenceQ(w, num, i):
    if not w[i:]:  
        return False
    if w[i] == num:
        return True
    return(pertenceQ(w, num, i+1))

print(pertenceQ([1,2,3],1,0))
print(pertenceQ([1,2,3],2,0))
print(pertenceQ([1,2,3],3,0))
print(pertenceQ([1,2,3],4,0))
