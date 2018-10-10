# 2 Defna a função div que recebe como argumentos dois números naturais m
#  e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não
# pode recorrer às operações aritmétcas de multplicação, divisão e resto da divisão
# inteira.
# Ex: div(7,2) = 3


div = lambda n,m: 0 if n < m else 1+div(n-m,m)

assert(div(7,2) == 3)
print(div(7,2))