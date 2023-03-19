n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

s = n1 + n2

print("A soma é: ", s)

############ OUTRO EXERCICIO

n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro valor"))

s = n1 + n2

#print("A soma entre",n1, "e",n2,"é igual a:", s )

#ou posso usar o recurso .format e aspas para evitar as aspas. 

print("A soma entre {} e {} é igual a {}".format(n1,n2,s))

############# COMENTÁRIOS
#Para fazer operações matemáticas, se nao sinalizar que a sentença é do tipo inteiro, ela entende como string. Para saber como o IDE está entendendo um valor, digite:
#n1 = input("Digite um valor: ")
#print(type(n1))

#para evitar isso, incluir int e parenteses no código.
#n1 = int(input("Digite um valor: "))
#print(type(n1))