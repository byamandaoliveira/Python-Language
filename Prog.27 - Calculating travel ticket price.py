#calculating travel ticket price
#01option
print("-=-"*20)
print("Travel ticket cost counter")
print("-=-"*20)
dist=float(input("What is the distance in kilometers of your trip?\n"))
print("Calculating fare...")
if dist < 200:
    cal1=float(dist*0.50)
    print("The cost of the ticket for your trip will be R${:.2f}.".format(cal1))
else:
    cal2=float(dist*0.45)
print("The cost of the ticket for your trip will be R${:.2f}.".format(cal2))
print("Good Trip!\n\n")

#02option
print("-=-"*20)
dist=float(input("What is the distance in kilometers of your trip?\n"))
print("Calculating fare...")
if dist <= 200:
    print(f"The cost of the ticket for your trip will be R${dist*0.5:.2f}.")
else:
    cal2=float(dist*0.45)
print(f"The cost of the ticket for your trip will be R${dist*0.45:.2f}.")
print("Good Trip!\n\n")

#03option
print("-=-"*20)
print("Travel ticket cost counter")
print("-=-"*20)
dist=int(input("What is the distance in kilometers of your trip?\n"))
print("Calculating fare...")
value= dist *0.50 if dist <= 200 else dist *0.45
print("The cost of the ticket for your trip will be R${:.2f}.".format(value))