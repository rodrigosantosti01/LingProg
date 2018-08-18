# Atividade - 7 
# João Papo-de-Pescador, homem de bem, comprou um
# microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50
# quilos8 deve pagar uma multa de R$ 4,00 por quilo excedente. João
# precisa que você faça um programa que leia a variável peso (peso
# de peixes8 e verifque se há excesso. Se houver, gravar na variável
# excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.


peso_peixe = int(input("digite o peso do peixe:"))
peso_excedente =0
valor_multa = 0.0
if (peso_peixe>50):
	peso_excedente = peso_peixe-50
	valor_multa = peso_excedente*4.00
	print ("De acordo com o regulamento de SP foi excedido %skg a mais do estabelecido e pagará %sR$ de multa"   %(peso_excedente,valor_multa))
else:
	print ("Não houve  peso em excesso %sKg portanto não há multa %sR$"  %(peso_excedente,valor_multa))