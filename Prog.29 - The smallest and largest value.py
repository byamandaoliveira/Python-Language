#Smallest and largest value entered
#1option
n1=int(input("Type a number 1:"))
n2=int(input("Type a number 2:"))
n3=int(input("Type a number 3:"))

if n1<n2 and n1<n3: #se n1 for menor que n2 e n1 for menor que n3
    menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print("The smallest value entered is {}.\n\n".format(menor))

#02option
n1=int(input("Type a number 1:"))
n2=int(input("Type a number 2:"))
n3=int(input("Type a number 3:"))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print("The smallest value entered is {} and the largest is {}.".format(menor, maior))