#calculate the hypotenuse of a right triangle
#01option
co=float(input("Type the opposite cathetus in centimeters: "))
ca=float(input("Type the adjacent cathetus in centimeters: "))
hypotenuse= (co**2 + ca**2)**(1/2)
print("The hypotenuse in centimeters is: {:.2f}.".format(hypotenuse))


#02option
b = float(input('\n\nInform the Cathetus Opposite: '))
c = float(input('Inform the Cathetus adjacent: '))
a = b**2 + c**2 
print(f'The hypotenuse is: {a**(1/2):.2f}')