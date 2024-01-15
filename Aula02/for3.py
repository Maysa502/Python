import os


cores = ["Rosa","Verde","Preto","Lilas","Azul","Cinza","Branco","Marrom"]
# print(cores[0]) se quiser uma cor especifica é colocar cores[posição da cor]. Lembrando o priemrio numero é 0.
os.system("clear")
# cls - ww 
# comando os da pra saber de mts coisas relacionada a maquina ospedeira

# for c in cores:
#     print("Eu gosto de "+c)
# # o '+c' sig que é a união das cores (variveis) + a frase = união de casório 

'''Aqui a gente ta fazendo duas variaveis de contagem a varia 'q(quant) e a variavel 'c(cores)'''
# Foi necessario fazer uma conversão, pra str pois ele tava entendendo que o q era uma equação e não uma contagem

q = 1
for c in cores:
    print(str(q)+ "ª cor é "+c) 
    # precicou colocar o str para converter o q, contatenou o 'q' a frase e o 'c'. O 'c' ta entrando dentro da lsita 'cores' 
    q=q+1
# o c ta no lugar do 'i' e o 'cores' no range. Ambos fazem o mesmo papel 
