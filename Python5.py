# estrutura de repetição while, será executado enquanto a condição for verdadeira

x = 1

while x <= 3:

    print(x)

    x = x + 1
print("Números de 1 até 100")
# Não exibirá 3 + 1, uma vez que 4 demonstra que a condição é False

y = 1

while y <= 100:

    print(y)

    y = y + 1


print("Número de 50 até 100")

z = 50

while z <= 100:
    
    print(z)

    z = z + 1

##################

print("Contagem regressiva de um foguete")

f = 11

while f > 1:

    f = f - 1
    print(f)
    
print("Fogo!")

#####################

end = int(input("Insira o último número da contagem: "))

e = 1

while e <= end:
    print(e)

    e = e + 1

#################
# números pares entre 0 e o dígito impresso pelo user

end = int(input("Digite o último número a imprimir pares: "))

x = 0
while x <= end:         #
    if x % 2 == 0:      # while x <= end:
        print(x)        # print(x)
    x = x + 1           # x = x + 2


n = int(input("Digite o último número a imprimir impares: "))

x = 0
while x <= n:
    if x % 2 == 1:
       print(x)
    x = x + 1

# 10 primeiro múltiplos de 3

#########

print("10 primeiros multiplos de 3")

m = 0
while m < 31:
       m += 1 # x = x + 1
       if m % 3 == 0:
        print(m)


##########

n = int(input("Tabuada de: "))

c = 1

while c <= 10:
 print(n * c)
 c = c + 1

##################

n = int(input("Tabuada de: "))

c = int(input("Começa em: "))

w = int(input("Termina em: "))

while c <= w:
 print(n * c)
 c = c + 1
###################
#5.8
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

x = 0
while n2 > 0:
    x = x + n1
    n2 = n2 - 1
print(x)
#########################
