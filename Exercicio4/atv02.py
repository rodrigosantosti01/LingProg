# 2 Mesma letra: Escreva uma função que receba uma string com duas palavras e
# retorne True se ambas palavras começarem com a mesma letra. Exemplo:
# mesma_letra('Cão covarde') -> True
# mesma_letra('Vira Lata') -> False


def comecam_com_a_mesma_letra(palavra):
	partes = palavra.split(" ");
	if partes[0][0].upper() == partes[1][0].upper():
		return True
	return False

resultado1 = comecam_com_a_mesma_letra("Cão covarde")
print(resultado1)

resultado2 = comecam_com_a_mesma_letra("Vira Lata")
print(resultado2)

	