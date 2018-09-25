	# 1 Linha: Crie a classe Linha que tem dois atributos, coordenada1 e coordenada2.
	# Cada coordenada é uma tupla que carrega duas coordenadas cartesianas (x,yg que
	# denotam pontos do segmento de reta. Faça métodos que calculem o comprimento
	# do segmento de reta e sua inclinação.


import math
class Linha:
    
    def __init__(self, c1, c2):
        self.coordenada1 = c1
        self.coordenada2 = c2
        
    def calcularComprimento(self):
        return math.sqrt((self.coordenada2[0] - self.coordenada1[0])**2 + (self.coordenada2[1] - self.coordenada1[1])**2)
    
    def calcularInclinacao(self):
        return (self.coordenada2[1] - self.coordenada1[1]) / (self.coordenada2[0] - self.coordenada1[0])
    
linha = Linha((5, 4), (8, 9))
print("comprimento", linha.calcularComprimento())
print("inclinação",linha.calcularInclinacao())