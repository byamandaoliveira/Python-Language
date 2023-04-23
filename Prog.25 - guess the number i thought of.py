from random import randint
computer = randint(0,5)
name = str(input("What's your name?\n"))
print ("-=-"*20)
print ("LET'S PLAY!\nI'll think of a number between zero and five!")
print ("-=-"*20)
usuario = int(input("{},What's number did I think??\n".format(name)))
if usuario == computer:
    print("Congratulations! You got the number I thought right!")
else:
    print("I won!!! I thought of the number {} and not the {}.".format(computer, usuario))