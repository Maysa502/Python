numero = input("Digite um numero: ")
# o comando input sempre retorna um valor em fomato texto, não importa se foi digitado um valor numerico, ele sempre retorna um texto
# sendo assim, foi necessario converter a variavel 'numero' para um valor inteiro. Neste caso, coloquei o int(inteiro na frente da vari)

    # se um "inteiro" "numero" for "dividido por 2" e o 'resto' for "semelhante" a "0":
if int(numero) %2 == 0: 
    print("O numero digitado é par")
else:
    print("O numero digitado é impar")


# outa forma de realizar este algoritimo é: Add a equação na variavel
    # numero = int(numero) %2 ==0
        # if (numero):
            # print("Este é um algarismo par")
        # else:
            # print("Este algorismo é impar")
