# Atividade - 12 
# Leet é uma forma de se escrever o alfabeto latino usando outros
# símbolos em lugar das letras, como números por exemplo. A própria
# palavra leet admite muitas variações, como l33t ou 1337. O uso do
# leet reflete uma subcultura relacionada ao mundo dos jogos de
# computador e internet, sendo muito usada para confundir os
# iniciantes e afrmar-se como parte de um grupo. Pesquise sobre as
# principais formas de traduzir as letras. Depois, faça um programa
# que peça uma texto e transforme-o para a grafa leet speak.
# Desafo: não use loops nem desvios condicionais.



texto = input("Digite um texto: ")
texto = texto.replace("a", "4")
texto = texto.replace("b", "ß")
texto = texto.replace("c", "¢")
texto = texto.replace("e", "3")
texto = texto.replace("f", "ƒ")
texto = texto.replace("g", "6")
texto = texto.replace("h", "[-]")
texto = texto.replace("i", "1")
texto = texto.replace("j", "¿")
texto = texto.replace("k", "x")
texto = texto.replace("l", "£")
texto = texto.replace("n", "/V")
texto = texto.replace("o", "0")
texto = texto.replace("p", "/*")
texto = texto.replace("q", "<|")
texto = texto.replace("r", "2")
texto = texto.replace("s", "5")
texto = texto.replace("t", "7")
texto = texto.replace("u", "µ")
texto = texto.replace("y", "≥")
print( texto)




# A	4 /\ @ ∂ /-\ |-\
# B	8 13 |3 ß
# C	( ¢ < [ ©
# D	[) |> |) |]
# E	3 € є [-
# F	|= ƒ /=
# G	6 (_+
# H	# /-/ [-] ]-[ )-( (-) :-: |~| |-| ]~[ }{
# I	1 ! | ][ ] :
# J	_| _/ ¿
# K	X |< |{ ɮ
# L	£ 1_ ℓ |_ [_
# M	|V| |\/| /\/\ /V\
# N	|V |\| /\/ [\] /V
# O	[] 0 () °
# P	|* |o |º |° /*
# Q	¶ (_,) ()_ 0_ °| <| 0.
# R	2 |? /2 ® Я |2
# S	5 $ § _/¯
# T	7 † ¯|¯
# U	(_) |_| L| µ
# V	\/ |/
# W	\/\/ vv '// \^/ \V/ \|/ \_|_/ \_:_/
# X	>< }{ × )(
# Y	`/ φ ¥ '/
# Z	≥ 7_ >_