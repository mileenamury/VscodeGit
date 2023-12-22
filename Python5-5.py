
casa = float(input("Qual o valor da casa?  "))

salario = float(input("Quanto você recebe?  "))

anos = input(input("Em quantos anos você quer financiar?  "))

prestação = casa / salario

trinta = salario - (0.3 * salario)

if prestação > trinta:
    print("Seu empréstimo não foi aprovado!")

else:
    prestação< trinta
    print(" Seu empréstimo foi aprovado, o valor da prestação mensal é R$%.2f" % prestação)

#####################

print("Preço do consumo de energia")
consumo = float(input("Qual a quantia de kWh consumida?  "))

print("1. R para residencia")
print("2. I para indústrias")
print("3. C para comércios")

tipo = float(input("Qual a tipo de instalação?  ")) 

if tipo == 1:
    if consumo > 500:
        c = consumo * 0.65
        print(" O preço a ser pago na residencia é ", c)

    else:
         consumo < 500
         c = consumo * 0.40
         print(" O preço a ser pago na residencia é ", c)

         if tipo == 2:

            if consumo > 5000:
               c = consumo * 0.6
               print(" O preço a ser pago pela industria é ", c)
            else:
                 consumo < 5000
                 c = consumo * 0.55
                 print(" O preço a ser pago pela industria é ", c)

                 if tipo == 3:
                     consumo > 1000
                     c = consumo * 0.6
                     print(" O preço a ser pago pelo comercio é ", c)

                 else:
                      consumo < 1000
                      c = consumo * 0.55
                      print(" O preço a ser pago pelo comercio é ", c)


