# Variavel de contagem 
# cuidado no print

qtd = 0 
for i in range(1,201):
    if i % 2 == 0:
        qtd = qtd + 1 
print("A quantidade de numeros pares entre 1 e 200 é ")
print(qtd




      
# Explicando o codigo com detalhes:
    # qtd = 0 - a variavel dando inicio na contagem, sem ela estipular o valor não roda
    # for i in range(1,201): - contagem de 1 a 200
        # if i % 2 == 0: - SE o resto da divisão for 0 significa que o numero é par 
            # qtd = qtd + 1 - Aqui é o pulo do gato; caso a divisão for par acrescenta +1 na quantiade de valor na variavel 'qtd'. Se não, a condição não se aplica e volta para o FOR. É por isso que essa condição esta depois do IF
                 # Em resumo: Se i não for par, o programa pula a instrução qtd = qtd + 1 e continua com o próximo valor de i no loop for
    # print("Essa é a quantidade de numeros pares" , qtd)

      
