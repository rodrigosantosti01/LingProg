# 7. Faça um programa que lê as duas notas parciais obtidas por um
# aluno numa disciplina ao longo de um semestre, e calcule a sua
# média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento Conceito
#  Entre 9.0 e 10.0 A
#  Entre 7.5 e 9.0 B
#  Entre 6.0 e 7.5 C
#  Entre 4.0 e 6.0 D
#  Entre 4.0 e zero E
# O algoritmo deve mostrar na tela as notas, a média, o conceito
# correspondente e a mensagem “APROVADO” se o conceito for A, B
# ou C ou “REPROVADO” se o conceito for D ou E.




nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a seguda nota: "))
media = abs((nota_um+nota_dois)/2)

print("Entre 9.0 e 10.0 A\n Entre 7.5 e 9.0 B\n Entre 6.0 e 7.5 C\n Entre 4.0 e 6.0 D \n Entre 4.0 e zero E \n")
print("Notas: %s %s" %(nota_um,nota_dois))
print("média %s" %(media))


if(media<6.0):
	print("REPROVADO")
	if(media<4.0):
		print("Conceito: D")
	elif(media>=4.0 and media<6.0):
		print("Conceito: E")

if(media>=6.0):
	print("APROVADO")
	if(media>=6.0 and media<7.5):
		print("Conceito C")
	elif(media>=7.5 and media <9.0):
		print("Conceito B")
	elif (media>=9.0 and 10.0):
		print("Parabéns! Conceito A")