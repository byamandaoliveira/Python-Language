#add up the school grades and calculate the arithmetic mean.
#1option

number1=float(input("Type a note: "))
number2=float(input("Type another note: "))
calculation=number1+number2
average=calculation/2
print("\nThe note 1 typed is: {}, the note 2 typed is: {} and the average is {}".format (number1, number2, average))

if average <7.0:
    print("Unfortunately, the student got {} average and failed!".format (average))
else:
    print("  Luckily, the student got a {} average and moved on to the next grade!".format(average))


#2option
n1=float(input("\n\nType a note: "))
n2=float(input("Type another note: "))
print(f"Result: \n - The sum of scores: {n1+n2} \n - The average is: {(n1+n2)/2}")




#I added if and else in the code to make it more complete.
#we can use integer numbers (int) or decimal numbers (float).