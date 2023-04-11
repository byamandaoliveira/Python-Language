#Primeiro e último nome de uma pessoa
#01option
name=str(input("Type your name complete: ")).strip()
n=name.split()
print("Nice too meet you!")
print("Your first name is: {}".format(n[0]))
print("Your last name is: {}".format(n[len(n)-1]))

#02option
nome = input('\n\nQual o seu nome completo? ')
m = nome.split()
print(f'Seu primeiro nome é {m[0]} e seu último nome é {m[-1]}')