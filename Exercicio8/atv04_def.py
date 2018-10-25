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



valor = 5
def cafe(f):
    def decorador(adc):
        return f(adc)
    return decorador 

def cafe_funcao(adc):
    return adc


cafe_funcao = cafe(cafe_funcao)

entrada = int(input("Menu: \n 1-Para Palitos de chocolate \n 2-Para espuma de leite \n 3-Para caramelo \n 4-Para Canela \n 0-Sair \n"))
while (entrada != 0):
    if (entrada ==1):
        print("chocolate")
        valor += cafe_funcao(0.50)
    if(entrada == 2):
        print("espuma de leite")
        valor += cafe_funcao(0.20)
    if(entrada == 3):
        print("Caramelo")
        valor += cafe_funcao(0.10)
    if (entrada ==4):
        print("Canela")
        valor  += cafe_funcao(0.30)
    entrada = int(input("Digite: \n 1-Para chocolate \n 2-Para espuma de leite \n 3-Para caramelo \n 4-Para Canela \n 0-Sair \n"))
print(valor)
