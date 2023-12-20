x = int(input("Numero 1: "))
y = int(input("NUmero 2: "))

w = 0
while x >= y:
   x = x - y
   w = w + 1

print("quociente",w)
print("resto", x)

############################

pontos = 0
questão = 1
while questão <=3:
    resposta = input("Resposta da questão %d: "% questão)
    if questão == 1 and (resposta == "b" or resposta == "B"):
       pontos += 1
    if questão == 2 and (resposta == "a" or resposta == "A"):
        pontos += 1
    if questão == 3 and (resposta == "d" or resposta == "D"):
        pontos += 1
    questão += 1

print(" o aluno fez %d ponto(s)" % pontos)
    
############
n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %d número:" %n))
    soma = soma + x #Acumulador, variavel
    n = n + 1      #Contador, fixo
print("Soma: %d" %soma)

#media aritmetica de cinco numeros com acumulador
m = 1
add = 0
while m <= 5:
    c = int(input("%d Digite o número: "% m))
    add =add + c #Acumulador, variavel
    m = m + 1      #Contador, fixo
print("Média: %5.2f" %(add/5))

######################

dep = int(input("Depósito inicial: "))

tx = float(input("A taxa de juros mensal da poupança: "))

x = int(input("A quantidade de meses: "))

rende = x *( dep * tx )

print(rende)

#####################
