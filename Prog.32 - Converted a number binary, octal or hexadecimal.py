#converter o numero em binario, octal ou hexadecimal.
print("-=-"*25)
print("\33[;43m HELLO, USER! \33[m")
print("-=-"*25)
num=int(input("Type a whole number, please!\n")) #digitar aspas triplas deixa eu inserir texto de print na proxima linha.
print('''Inform which conversion base you want to view:
Enter 1 for binary.
Enter 2 for octal.
Enter 3 for hexadecimal.''')
opcao = int(input('Your option: '))
if opcao == 1:
    print("{} converted to BINARY is equal to {}.".format(opcao, bin(num)[2:]))
elif opcao == 2:
    print("{} converted to OCTAL is equal to {}.".format(opcao, oct(num)[2:]))
elif opcao == 3:
    print("{} converted to HEXADECIMAL is equal to {}.".format(opcao, hex(num)[2:]))
else:
    print("Invalid option! Try again!")