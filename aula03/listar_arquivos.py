import os

os.system("cls")

# retorna uma lista contendo os nomes de um arquivo num diretório
# print(os.listdir("c:/"))
#       o local do arquivo
# print mostra as lista, em py [] - é uma lista
# a melhor forma de ler uma lista é atraves de uma estrutura de repição

lst = (os.listdir("c:/"))

ps = 1

for i in lst:
    print(str(ps)+"º - "+i)
    ps+=1 

esc=input("Digite o numero correspondete a pasta que deseja ver: ")

match esc:
    case "1":
        print(os.listdir("c:/$Recycle.Bin"))
    case "2":
        print(os.listdir("c:/$WinREAgent"))
    case "3":
        print(os.listdir("c:/3A3C7B3F7DBF"))
    case "4":
        print(os.listdir("c:/adobeTemp"))
    case "5":
        print(os.listdir("c:/Arquivos de Programas"))
    case "6":
        print(os.listdir("c:/Documents and Settings"))
    case "7":
        print(os.listdir("c:/DumpStack.log"))
    case "8":
        print(os.listdir("c:/DumpStack.log.tmp"))
    case "9":
        print(os.listdir("c:/eclipse"))
    case "10":
        print(os.listdir("$Windows"))
    case "12":
        print(os.listdir("c:/Recovery"))
    case _:
        print("Diretório não localizado")
   