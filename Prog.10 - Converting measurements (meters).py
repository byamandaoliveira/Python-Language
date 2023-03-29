#converting measurements (meters)
#1option
value=float(input("Type a value in meters: "))
print(f"Converter: \n - This value correspondent the {value*100} in centimeters. \n - This value correspondent the {value*1000} in milimeter.")

#2option
valor=float(input("\n\nType a value in meters: "))
cent=valor*100
mili=valor*1000
print("Converter: \n - This value correspondent the {} in centimeters. \n - This value correspondent the {} in milimeters.".format(cent, mili))
