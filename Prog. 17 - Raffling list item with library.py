#Raffling list item with library
#01option
import random
n1=str(input("Type the firts name: "))
n2=str(input("Type the second name: "))
n3=str(input("Type the thirf name: "))
n4=str(input("Type the fourth name: "))

list=[n1,n2,n3,n4]
chosen = random.choice(list)

print("The name raffle is: {}.".format(chosen))


#02option
from random import choice
student = input('\n\nWrite students' names separated by space and comma: ').split(", ")
print('\nThe chosen student was: {}'.format(choice(student)))