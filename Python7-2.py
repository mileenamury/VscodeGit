
maior = 0

n = int(input("Insira um número: "))

while n != 0:
    if n > maior:
        maior = n
    n = int(input("Insira um número:"))

print("O maior número é %d"%(maior))

##################

for m in range(1, 11):
     print(m)
     if m % 10  == 0:
        print("Múltiplo de 10: %d"%(m))

###############

for h in range (100, 201):
   if h %2 != 0:
    print("Ímpar: %d"%(h))

##################

maior = 0
menor = 0
soma = 0

for c in range (0,10):
    valor = int(input("Insira o valor: "))
    if valor  > 0:
        if valor > maior:
            maior = valor
        
        if valor < menor:
            menor = valor 

    soma = soma + valor

else:
    valor = int(input("Informe um valor: "))

    media = soma /10

print("O maior é %d"%(maior))
print("O menor é %d"%(menor))
print("A média é %d"%(media))

###################################