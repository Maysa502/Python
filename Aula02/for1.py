# Vanos fazer uma contagem de 1 até 10

# _step é de quanto em quanto até contar
# só um valor ele ta fazendo um _stop

    # for variavel in sequencia:
for i in range(1,11):
    print(i)
# essa for vai de 1 (valor inicial) e até 10 (valor final 11) pois o ultimo indice sempre é excluido
# a convenção de excluir o último valor ao usar range em Python e a convenção de começar a indexação a partir de 0 são escolhas que visam reduzir erros e melhorar a consistência na linguagem


# ele começa sempre pelo 0, se quiser contar de um especifico coloca 'variavel+1'
i = 17
for i in range(i):
    print(i)
#  aqui vai contar de 0 até 17
