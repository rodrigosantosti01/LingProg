# Atividade - 9 
# Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings
# possuem o mesmo comprimento e são iguais ou diferentes no
# conteúdo.
# Exemplo:
# String 1: Brasil Hexa 2018
# String 2: Brasil! Hexa 2018!
# Tamanho de "Brasil Hexa 2018": 16 caracteres
# Tamanho de "Brasil! Hexa 2018!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.



string_um = input("digite uma string: ")
string_dois = input("digite outra string: ")
print ("String 1 : %s" %string_um)
print ("String 1 : %s" %string_dois)
print ('O tamaho de "%s": %s' %(string_um,len(string_um)))
print ('O tamaho de "%s": %s' %(string_dois,len(string_dois)))

if (len(string_um)==len(string_dois) and string_um == string_dois):
	print ("As duas strings são de tamanhos iguais.")
	print ("As duas strings  possuem conteudos iguais.")


if (len(string_um)==len(string_dois) and string_um != string_dois):
	print ("As duas strings são de tamanhos iguais.")
	print ("As duas strings possuem conteudos diferentes.")

else:
	print ("As duas strings são de tamanhos diferentes.")
	print ("As duas strings possuem conteudos diferentes.")