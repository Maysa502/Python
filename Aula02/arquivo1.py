# importar a biblioteca os(Sistema Operacional)
import os

# limpar a tela
os.system("clear")

arq = open("./texto.txt","w")
arq.write("Hoje é quarta-feira\nultima semanda de novembro")
arq.close() 

'''arq = open("./texto.txt","r") = ainda n tem o arq, necessario cria-lo'''
# arq.write("ESCREVE O QUE TA dentro do arqu ARQ TEXTO")