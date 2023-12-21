idade = int(input(print("Qual a idade em anos do seu carro?")))


if idade <= 3:

    print("Seu carro é novo")
else:

    print("Seu carro é velho")

#########


distancia = int(input(print("Qual a distancia a ser percorrida em km? ")))


if distancia <= 200:

    passagem = distancia * 0.50

    print("O preço da passagem é R$%d"%(passagem))
else:

    passagem = distancia * 0.45

    print("O preço da passagem é R$%d"%(passagem))

#############################


#estruturas aninhadas

#utilizar um if dentro de outro


minutos = int(input(print("Quantos minutos você utilizou esse mês:")))

if minutos < 200:

    preço = 0.20
else:

    if minutos < 400:

        preço = 0.18
    else:

        preço = 0.15

print("Você vai pagar no mes atual R$%6.2f" % (minutos * preço))

##########


categoria = int(input("Digite a categoria do produto:"))

if categoria == 1:

        preço = 10
else:

    if categoria == 2:

        preço == 18
    else:

        if categoria == 3:

            preço = 23
        else:

            if categoria == 4:

               preço = 26
            else:

                if categoria == 5:

                   preço = 31
                else:

                    print("Categoria inválida, digite um valor entre 1 e 5!")

                    preço = 0

print("O preço do produto é: R$%6.2f" % preço)


#############################


# a cláusula elif substitui um par if else, sem criar outro nível de estrutura


categoria = int(input("Digite a categoria do produto:"))

if categoria == 1:

    preço = 10

elif categoria == 2:

    preço == 18

elif categoria == 3:

    preço = 23

elif categoria == 4:

     preço = 26

elif categoria == 5:

     preço = 31
else:

     print("Categoria inválida, digite um valor entre 1 e 5!")

     preço = 0

print("O preço do produto é: R$%6.2f" % preço)

#############

print("Calculadora")

print("1.Adição")
print("2.Substração")
print("3.Multiplicação")
print("4.Divisão")

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))

operation = int(input("Qual operação você deseja realizar?  "))

if operation == 1:
    c = (n1 + n2)
    print("adição = ", c)

elif operation == 2:
    c = ( n1 / n2)
    print("Divisão = ", c)

elif operation == 3:
    c = (n1 * n2)
    print("multiplicação = ", c)

elif operation == 4:
    c = (n1 - n2)
    print("Subtração = ", c)
else:
    print("Escolha inválida")

    