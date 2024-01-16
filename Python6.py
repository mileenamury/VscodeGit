# P[0], P means the name and [0] the index

notas = [6,7,5,8,9]

soma = 0
x = 0

while x < 5:
    soma += notas[x]
    x += 1
print("Média: %3.1f" % (soma/x))

#######

v = float(input("Insira o valor: "))

if v > 100:
    print(v)
else:
   v = 0
   print("O valor é menor que 100: %d"% (v))

   ######################

y = float(input("Digite um número positivo ou negativo:"))

if y > 0:
    a = y
    print("O valor é positivo e pertence a: %d"%(a))
    
else:
     b = y
     print("O valor é negativo e pertence b: %d"%(b))

############################

w = int(input("Insira um valor: "))

if w % 2 == 0:
    p = w
    print("O valor é par e está armazenado em P: %5.3d"%(p))

else:
    i = w
    print("O valor é ímpar e está armazenado em I: %6.1d"% (i))

################################

s = input("Caso se identifique com um sexo binário, digite qual: ")
a = float(input("Insira sua altura em metros (Ex: 1.86): "))

if s == 'F' or s == 'f' or s == 'feminino':
    p_ideal = (62.1 * a) - 44.7

else:
    s == 'M' or s == 'm' or s == 'masculino'
    p_ideal = (72.7 * a) - 58

print("O seu peso ideal é: %5d" % (p_ideal))


######################################

weight = float(input("Insira a pesagem: "))

e = 0
m = 0

if weight > 50:
    e = weight - 50
    m = e * 4

print("O peso é %d, a multa %2d e o excesso %2d"%(weight, m, e))

#6.6

