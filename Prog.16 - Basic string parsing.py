#basic string parsing
#01option
name=str(input("Type your name complete: ")).strip()
print("Analyzing your name... ")
print("Your name uppercase is: {} ".format(name.upper()))
print("Your name lowercase is: {} ".format(name.lower()))
list=name.split()
print("Your first name is:  {}".format(list[0]))
print("Your name has {} caracteres".format(len(name)))

#02option
nome = input('\n\nType your name complete: ').strip()
print("Analyzing your name...")
print(f'Your name uppercase is: {nome.upper()}\n'
      f'Your name lowercase is: {nome.lower()}\n'
      f'Your name complete has: {len(nome) - nome.count(" ")}letters\n'
      f'Your first name has is: {nome.find(" ")} letters. ')