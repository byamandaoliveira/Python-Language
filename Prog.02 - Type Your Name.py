nome = input("Type your name: ")
print("\nWelcome a my code, %s!" %nome)

#outra forma de realizar é:

nome = input("\nType your name: ")
print("\nWelcome a my code,{}!".format(nome))

#No primeiro código, eu usei uma mascara de formatação. No caso, o porcento s. 
#No segundo código, as chaves sao uma saida formatada. Quando utilizar as chaves, lembrar de incluir o ponto format e nomear a variavel que deve ser mostrada.