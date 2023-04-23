#
#01option
print("-=-"*20)
print("RADAR AND FINE")
print("-=-"*20)
veloc=int(input("Hello, what's is the veloicty in the vehicle?\n"))
dif=int(veloc - 80)
val=int(7)
mult=float(dif*val)
print("This street allow velocity from to 80km/h!")
if veloc > 80:
    print("Unfortunately, the driver did not respect the sign. You will receive a fine of R${:.2f} for exceeding the permitted speed!".format(mult))
else:
    print("Congratulations, the driver is respecting the road signs!")

#02option
print("-=-"*20)
print("RADAR AND FINE")
print("-=-"*20)
veloc=int(input("Hello, what's is the veloicty in the vehicle?\n"))
if veloc > 80:
    fine=(veloc-80)*7
    print("Unfortunately, the driver did not respect the sign. You will receive a fine of R${:.2f} for exceeding the permitted speed!".format(fine))
elif veloc < 40:
    print(
        "Unfortunately, the driver did not respect the sign. You will be fined for driving too slowly!!")
else:
    print("Congratulations, the driver is respecting the road signs!")
print("Have a good day and drive carefully!")