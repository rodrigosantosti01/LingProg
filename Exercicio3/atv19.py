# 19. A série de Fibonacci é formada pela seqüência
# 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série
# até o n−ésimo termo


a = 0
b = 1
nesimo = int(input("Até qual termo? "))
for i in range(nesimo):
    print(a)
    aux = b
    b = a + b
    a = aux