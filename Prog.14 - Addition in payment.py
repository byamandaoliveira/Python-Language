#addition in payment
#1option
value=float(input("Inform the value of payment:"))
print(f"The payment {value} with addition of 15%, became the value of: {(value + (value*0.15)):.2f} dollars.")

#2option
value=float(input("\n\nInform the value of payment: "))
now=value+(value*0.15)
print("The payment {:.2f} with addition of 15%, became the value of: {} dollars.". format(value, now))