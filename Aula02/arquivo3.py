# este arquivo esta lendo os dados feitos no info.csv

import os
os.system("clear")

#korra = nome da variavel do arq
korra = open("./arquivos/info.csv")
print(korra.read())
korra.close()
