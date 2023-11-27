'''
Crie um programa para mostrar se o aluno esta 
aprovado, reprovado ou em recuperação.
O programa deve pedir 4 notas e realizar o calculo da media 
Se a media for:

>= 6 -> Aprovado
<= 4 -> Reprovado
>4 e <6 -> Recuperação
'''
primb = float (input("Digite a nota do aluno: "))
segb = float (input("Digite a nota do aluno: "))
tercb = float (input("Digite a nota do aluno: "))
quarb = float (input("Digite a nota do aluno: "))

media = (primb + segb + tercb + quarb) / 4


media = float(media) 
if media >= 6:
    print("Aluno aprovado")
elif media <= 4:
    print ("Aluno reprovado")
else:
    print("Aluno em recuperação")


