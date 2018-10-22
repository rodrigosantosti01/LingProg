# 2. Escreva uma função que recebe uma lista de triplas e, para cada uma, gera uma
# equação do segundo grau considerando que os elementos da tripla são os
# coefcientes usualmente denominados a, b e c da equação. Note que a sua função
# deverá devolver uma lista de equações. A geração das equações deve ser feita por
# meio de, evidentemente, decorators.


def coefcientes (a, b, c):
	def eq_seg_grau (x):
	return a * (x * x) + b * x + c
return eq_seg_grau





print ( coefcientes(1, 2, 3) (1))