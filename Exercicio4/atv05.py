# 5 Blackjack: Faça uma função que receba 3 inteiros entre 1 e 11. Se a soma deles for
# menor que 21, retorne o valor da soma. Se for mair do que 21 e houver um 11, 
# subtraia 10 da soma antes de apresentar o resultado. Se o valor da soma passar de
# 21, retorne ‘ESTOUROU’. Exemplo:
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'ESTOUROU'
# blackjack(9,9,11) --> 19


def blackjack(a,b,c):
	soma=a+b+c
	if soma <= 21:
		return soma
	else:
		if 11 in [a,b,c]:
			return soma - 10
		return ('ESTOUROU',soma)

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))