# 2. Faça um Programa que verifque se uma letra digitada é vogal ou
# consoante.

letra = input("Digite uma letra: ")

if(letra.lower()=='a' or letra.lower()=='e' or letra.lower()=='i' or letra.lower()=='o' or letra.lower()=='u'  ):
	print("Essa letra '%s' é uma vogal" %(letra))
else:
	print("Essa letra '%s' é uma consoante" %(letra))