#breaking a number in decimal
#01option - no matter
valor=float(input("Type a decimal number: "))
int= int(valor)
print("The number typed is {} and the integer part of the number is: {}.".format(valor, int))

#02option - importing the library "math"
import math
num = float(input("\n\nType a decimal number: "))
int = math.trunc(num)
print('The number typed is {} and the integer part of the number is {}.'.format(num,int))

#3option - importando o comando da biblioteca
from math import trunc
number = float(input('\n\nType a decimal number: '))
print(f'The integer part of the number {number} is: {trunc(number)}')

#4option - sem importar nada
valor = float(input('\n\nType a decimal number: '))
print(f'The number typed is {valor} and the integer part of the number is {valor.__trunc__()}')
