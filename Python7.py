n1 = int(input("Insira o valor:"))

if n1 % 2 == 0:
    p = n1
    print("O número %d é par" %(p))

else:
    i = n1
    print(" O valor %d é impar"%(i))
# Seção 6 parte 3 #

#################################################
#Seção 6 parte 6

n = int(input("Insira a quantidade de horas trabalhadas:"))

c = int(input("Insira seu código:"))

if n > 50:
    e = n - 50
    n = n - e
    s = n * 10
    s1 = e * 20
    print("O seu salário é %d e o salário excedente é %d"%(s, s1))

else:
    e = 0
    s = n * 10
    print("O seu salário é %d"%(s))

############

n11 = int(input("Insira o valor de n1:"))
n2 = int(input("Insira o valor de n2:"))
n3 = int(input("Insira o valor de n3:"))
n4 = int(input("Insira o valor de n4:"))

q1 = n11 ** 2
q2 = n2 ** 2
q3 = n3 ** 2
q4 = n4 ** 2

if q3 >= 1000:
    print(q3)

else:
    print(q1)
    print(q2)
    print(q3)
    print(q4)