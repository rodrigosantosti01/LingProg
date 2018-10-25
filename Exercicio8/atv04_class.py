# 4. Escreva uma classe para representar um café que, a princípio, tem somente preço.
# Um cafezinho custa 5 reais. 
# Escreva classes para representar os adicionais: palitos de
# chocolate (0,50 cents), espuma de leite (0,20 cents), caramelo (0,10 cents) e canela
# (0,30 cents). 
# Crie um objeto café e, a seguir, faça um menuzinho em que o usuário
# pode fcar indefnidamente escolhendo adicionais: 1 para chocolate, 2 para espuma
# de leite, 3 para caramelo e 4 para canela.
# A cada adicional escolhido, decore o objeto
# café. No fnal, mostre o preço total.



class Cafe:
    def __init__(self,preco=5):
        self.preco = preco

    def __call__(self,adicional):
        self.preco = self.preco + adicional.preco
        return self.preco

class Chocolates:
    def __init__ (self,chocolate):
        self.preco = chocolate
class EspumaLeite:
    def __init__ (self,leite):
        self.preco = leite
class Caramelo:
    def __init__ (self,caramelo):
        self.preco = caramelo
class Canela:
    def __init__ (self,canela):
        self.preco=canela

cafe = Cafe()
entrada = int(input("Menu: \n 1-Para Palitos de chocolate \n 2-Para espuma de leite \n 3-Para caramelo \n 4-Para Canela \n 0-Sair \n"))

while (entrada != 0):
    if (entrada ==1):
        print("chocolate")
        cafe(Chocolates(.50))
    if(entrada == 2):
        print("espuma de leite")
        cafe(EspumaLeite(.20))
    if(entrada == 3):
        print("Caramelo")
        cafe(Caramelo(0.10))
    if (entrada ==4):
        print("Canela")
        cafe(Canela(0.30))
    entrada = int(input("Digite: \n 1-Para chocolate \n 2-Para espuma de leite \n 3-Para caramelo \n 4-Para Canela \n 0-Sair \n"))
print(cafe.preco)

