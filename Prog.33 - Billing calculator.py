#billing calculator
print("-=-"*25)
print("\33[33m HOME INSTALLMENT SIMULATOR \33[m")
print("-=-"*25)
print(">>>  Let's Go!  <<<")
casa=float(input("What is the price of the house? "))
sal=float(input("what is your salary R$: "))
anos=int(input("In how many years would you like to pay off the house?"))
prest=casa / (anos*12)
maximo=sal * (30/100) #não pode exceder 30% do salario da pessoa.
print("To pay off a house worth R${} in {} years, the installment will be R${}.".format(casa, anos, prest))

if prest <= maximo:
    print("\33[32mCongratulations! Installment amount approved! \33[m")
else:
    print("\33[31mUnfortunately the value of your installment is below our normal and therefore it was denied. \33[m")