n1 = int(input("Insira o valor:"))

if n1 % 2 == 0:
    p = n1
    print("O número %d é par" %(p))

else:
    i = n1
    print(" O valor %d é impar"%(i))

if n1 > 0:
    print("%d é positivo"%(n1))
    
else:
    n1 < 0
    print("%d é negativo"%(n1))

##################

i = float(input("Insira o índice de poluição. Por exemplo, 0.3 :"))

if i >= 0.3 and i< 0.4:
    print("Grupo 1, suspenda as atividades!")

    if i >= 0.4 and i< 0.5:
        print("Grupo 1 e 2, suspendam as atividades!")

        if i >= 0.5:
            print("Todos os grupos, suspendam as atividades!")

else:
    print("Nível aceitável")

##############################

id = int(input("Insira sua idade: "))

if id >= 5 and id < 7:
    print("infantil A")

    if id >= 8 and id < 11:
        print("Infantil B")

        if id >= 12 and id < 13:
            print("Juvenil A")

            if id >= 14 and id < 17:
                print("Juvenil B")

else:
    id >= 18
    print("Adulto")





