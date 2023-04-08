#Classificando e separando um número 
#01option
num=int(input("Type the number between 0 and 9999: "))
n=str(num)
print("Analyzing the number...")
print("Unidade: {} ".format(n[3]))
print("Dezena: {} ".format(n[2]))
print("Centena: {} ".format(n[1]))
print("Milhar: {} ".format(n[0]))

#02option
num=int(input("\n\nType the number between 0 and 9999: "))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print("Analyzing the number...")
print("Unidade: {} ".format(u))
print("Dezena: {} ".format(d))
print("Centena: {} ".format(c))
print("Milhar: {} ".format(m))