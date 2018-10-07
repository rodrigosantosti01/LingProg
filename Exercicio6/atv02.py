# 2- Defna a função div que recebe como argumentos dois números naturais m
#  e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não
# pode recorrer às operações aritmétcas de multplicação, divisão e resto da divisão
# inteira.


def div(n,m):
	return 0 if n <	 m else 1+div(n-m,m)
print(div(7,2))
print(div(2,2))
print(div(1,2))
