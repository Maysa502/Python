import os

# n é legal o usuario escrever mt coisa no sistema - tem q interfirir o minimo possivel

os.system("cls")
print("Temos dois arquivos: bloco_texto e dados.txt")
print("Qual deles vocês deseja apagar?")
es = input("Digite: \n - 1 para bloco_texto\n - 2 para dados.txt\n :")

P = input("Você tem certeza que quer apagar o arquivo?[s,n]:")

if P == "s":
    if es == "1":
        os.remove("bloco_texto.txt")
    else: 
        os.remove("dados.txt")
    print("O arquivo foi apagado com sucesso")
else:
    print("Operação cancelada")