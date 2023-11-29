import os


cores = ["Rosa","Verde","Preto","Lilas","Azul","Cinza","Branco","Marrom"]
# print(cores[0]) se quiser uma cor especifica é colocar cores[posição da cor]
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
    q=q+1
