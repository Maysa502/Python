import os
os.system("clear")

arq = open("./arquivos/dados.csv","a")
nome = input("Digite o seu nome: ")
email = input("Digite o seu email: ")

# arquivos csv separa as coisa por ponto e virgula (;), ptn acha q ; é comando, então é necessario contaternar (+";") 
arq.write(nome+";"+email+"\n\r")
arq.close()

'''Aqui o arquivo não esta acrescentando os dados pelo comando arq = open("./arquivos/dados.csv","w")
necessarioa acrescentar o modo "a"
e colocar o quebra linha (+"\n\r") '''