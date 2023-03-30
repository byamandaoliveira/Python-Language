#quantity of paint to paint (converter)

lar=float(input("Whats is the width of your wall? "))
alt=float(input("Whats is the heigth of your wall?"))

print(f"\nYour wall has the dimension of: {lar}x{alt} and area is {lar*alt}cm².")
print(f"The paint the wall your will need of {(lar*alt)/2} liters of paint.")