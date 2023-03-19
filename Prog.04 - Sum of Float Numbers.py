n1 = float(input("Type a number: "))
n2 = float(input("Type another number: "))

s = n1 + n2

print("The sum of {} and {} is: {}".format(n1, n2, s))

############# COMENTÁRIOS
#Para fazer operações matemáticas, se nao sinalizar que a sentença é do tipo inteiro, ela entende como string. Para saber como o IDE está entendendo um valor, digite:
#n1 = input("Digite um valor: ")
#print(type(n1))

#para evitar isso, incluir int e parenteses no código.
#n1 = int(input("Digite um valor: "))
#print(type(n1))