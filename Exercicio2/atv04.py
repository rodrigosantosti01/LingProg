# Atividde - 04 

# Faça um programa que percorre uma lista com o seguinte
# formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]],
# ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que
# cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e
# Itália, o Brasil fez 10 faltas e a Itália fez 9.
# O programa deve imprimir na tela:
# - o total de faltas do campeonato
# - o time que fez mais faltas
# - o time que fez menos faltas




tabela1 = ['Brasil', 'Italia', [10, 9]]
tabela2 = ['Brasil', 'Espanha', [4, 7]]
tabela3 = ['Italia', 'Espanha', [7,8]]
campeonato = [tabela1, tabela2 ,tabela3]
faltas = []
for  i  in campeonato:
	faltas.append(sum(i[2]))
print ("Total de faltas no campeonado %s" %(sum(faltas)))

faltas_Brasil = 0
faltas_Italia = 0 
faltas_Espanha = 0
contagem = 0
for j in tabela1,tabela2,tabela3:
	if (j[0]=='Brasil' or j[1]=='Brasil'):
		 faltas_Brasil +=(j[2][0])
	if(j[0]=='Italia' or j[1]=='Italia'):
		aux = (tabela1[2][1])
		faltas_Italia = (tabela3[2][0])
		faltas_Italia = aux + faltas_Italia
	if (j[0]=='Espanha' or j[1]=='Espanha'):
		faltas_Espanha +=(j[2][1])

if (faltas_Brasil > faltas_Espanha and faltas_Brasil > faltas_Italia):
	print ("Brasil: %s" %(faltas_Brasil))
if (faltas_Italia > faltas_Espanha and faltas_Italia > faltas_Brasil):
	print ("Italia: %s" %(faltas_Italia))
if ( faltas_Espanha > faltas_Brasil and faltas_Espanha > faltas_Italia):
	print ("Espanha: %s" %(faltas_Espanha))

if (faltas_Brasil < faltas_Espanha and faltas_Brasil < faltas_Italia):
	print ("Brasil: %s" %(faltas_Brasil))
if (faltas_Italia < faltas_Espanha and faltas_Italia < faltas_Brasil):
	print ("Italia: %s" %(faltas_Italia))
if ( faltas_Espanha < faltas_Brasil and faltas_Espanha < faltas_Italia):
	print ("Espanha: %s" %(faltas_Espanha))
