# forming triangles.
print("-=-"*25)
print("TRIANGLE ANALYZER")
print("-=-"*25)
l1=float(input("Enter the length of the first side: \n"))
l2=float(input("Enter the length of the second side: \n"))
l3=float(input("Enter the length of the third side: \n"))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print("The length of the informed sides FORM A TRIANGLE!"")
else:
    print("The size of the informed sides do not FORM A TRIANGLE!"")