#First and last occurrence of a string
#01option
frase=str(input("Type a sentence: ")).strip().upper()
print("QUantas vezes aparece a letra A: {}".format(frase.count('A')))
print("Em que posição aparece a primeira letra A: {}".format(frase.find('A')+1))
print("Em que posição aparece a última letra A: {}".format(frase.rfind('A')+1))

#02option com printf
n = input('\n\nDigite algo: ').upper().strip()
print(f'A letra "A" aparece {n.count("A")} vezes.')
print(f'A primeira letra A apareceu na posição {n.find("A")+1}.')
print(f'A ultima letra A aparece na posição {n.rfind("A")+1}.')
