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




def chocolate(f):
    def decorador():
        return  0.5 + f()
    return decorador 

def espumaLeite(f):
    def decorador():
        return  0.2 + f()
    return decorador 



def caramelo(f):
    def decorador():
        return  0.3 + f()
    return decorador 

def caramelo(f):
    def decorador():
        return  0.3 + f()
    return decorador 

def canela(f):
    def decorador():
        return  0.1 + f()
    return decorador 

def cafe ():
    return 5



entrada = int(input("Menu: \n 1-Para Palitos de chocolate \n 2-Para espuma de leite \n 3-Para caramelo \n 4-Para Canela \n 0-Sair \n"))
while (entrada != 0):
    if (entrada ==1):
        print("chocolate")
        cafe= chocolate(cafe)
    if(entrada == 2):
        print("espuma de leite")
        cafe = espumaLeite(cafe)
        print(cafe())
    if(entrada == 3):
        print("Caramelo")
        cafe = espumaLeite(cafe)
    if (entrada ==4):
        print("Canela")
        cafe = espumaLeite(cafe)
    entrada = int(input("Digite: \n 1-Para chocolate \n 2-Para espuma de leite \n 3-Para caramelo \n 4-Para Canela \n 0-Sair \n"))
print(cafe())