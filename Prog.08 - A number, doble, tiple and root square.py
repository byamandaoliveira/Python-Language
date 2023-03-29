#type a number, doble, tiple and root square
#1option
number=int(input("type a number: "))
doub=number*2
trip=number*3
root=number**(1/2)
print(f"The number entered is {number}, \nThe doube is: {doub}, \nThe triple is: {trip} \nAnd square root {root}")

#2option
number=int(input("\n\nType a number: "))
print(f"The number is: {number}, the double is: {number*2}, the triple is: {number*3} and root square is: {number**(1/2)}.")

#3option
number=int(input("\n\nType a number:"))
print("The number is: {}, the double is: {}, the tiple is: {} and root square is: {}.".format(number, (number*2), (number*3), (number**(1/2))))