# 5.11 
dep = int(input("Depósito inicial: "))

tx = float(input("A taxa de juros mensal da poupança em 24 meses: "))

rende = ( dep  * tx )

w = 1
while w <= 24:
    x = rende * w
    w = w + 1
    print( x)

y = rende * 24

print(" O total é %d "% (y))

#######################

# Valor depositado em cada mês
mensal = int(input("Qual a quantia depositada em cada mes? "))

dep = int(input("Depósito inicial: "))

tx = float(input("A taxa de juros mensal da poupança em 24 meses: "))

rende =  (dep + mensal) * tx 

w = 1
while w <= 24:
    x = rende * w
    w = w + 1
    print( x)

y = rende * 24

print(" O total é %d "% (y))

####################

d = int(input("Qual o valor inicial da dívida? "))

j = float(input("Insira o juro mensal: "))

m = int("Qual valor é pago mensalmente? ")



print("A dívida será paga em %d meses, total pago %d, total de juros pago %d"%())