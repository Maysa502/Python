''' Aqui é um exemplo de match case: 
A sintaxe match case é útil quando você tem várias opções ou casos diferentes a considerar, como em uma situação de escolha, 
decisão ou correspondência de padrões, em um visual mais claro, imagine que um usuario tem varias opções de cadastro, essa sintaxe
é bem util de otimizar os codigos''' 

dia = input("Digite um numero entre 1 e 7, e lhe diremos qual o dia da semana: ")

match dia:
    case '1': 
        print("Domingo")
    case '2':
        print("Segunda-feira")
    case '3':
        print("Terça-feira")
    case '4':
        print("Quarta-feira")
    case '5':
        print("Quinta-feira")
    case '6':
        print("Sexta-feira")
    case '7':
        print("Sabado")
    case _:
        print("Este dia da semana não existe ☺ ♥")
