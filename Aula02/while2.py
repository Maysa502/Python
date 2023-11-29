soma = 0
num = 1

while( num <= 50 ):
    if num % 2 == 0:
        soma+=num
    num+=1
# n esquecer a indicação do num; neste caso o num vai ser 1 forever 
print("A soma dos pares entre 1 e 50 é:"+str(soma))