#Sorting ordem
#01option
import random
n1=str(input("Type a name: "))
n2=str(input("Type a name: "))
n3=str(input("Type a name: "))
n4=str(input("Type a name: "))
list=[n1, n2, n3, n4]
random.shuffle(list)
print("The ordem is: ")
print(list)