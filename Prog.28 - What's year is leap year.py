#calculating travel ticket price
#01option
ano = int(input("What year would you like to review?\n"))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #tem que ser divisivel por 4 e tambem nao pode ser divisivel por 100 e diferente de zero ou ser divisivel por 400:
    print("The year {} is a leap year!".format(ano))
else:
    print("The year {} is not a leap year!".format(ano))