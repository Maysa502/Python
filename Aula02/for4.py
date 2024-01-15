# quantidade de anos bissextos de 1973 até 2023

#UwU
# Nesse algotimo mostra a quantidade de anos bissextos entre 1973 até 2023
qtd = 0 
for i in range(1973,2024):
    if i % 4 == 0:
        qtd = qtd + 1 
print("A quantidade de anos bissexto entre 1973 até 2024 é:",qtd)
                                                                                                           # no de cima o print é uma função do FOR

# Ja neste algoritmo mostra quais são os anos bissextos, isso acontece devido a maneira que colocamos o print, neste aqui colocamos abaixo da equação, dentro do IF 
q = 0
for i in range(1973,2024):
    if i % 4 == 0:
        q = q + 1
        print("A lsta de anos bissextos entre 1973 até 2024 é: " + str(i))
