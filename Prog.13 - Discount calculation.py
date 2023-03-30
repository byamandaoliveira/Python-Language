#discount calculation
#1option
value=float(input("Inform the value of produt:"))
print(f"The produt that use to cost {value:.2f} dollars, with a discont of 5% now costs: {(value*0.05):.2f} dollars.")

#2option
value=float(input("\n\nInform the value of produt: "))
now=value*0.05 #5% of discont
print("The produt that use to cost {:.2f} dollars, with a discont of 5%, now costs: {} dollars.". format(value, now))