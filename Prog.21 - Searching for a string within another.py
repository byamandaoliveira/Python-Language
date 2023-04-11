#Searching for a string within another
#01option
name=str(input("What's your complet name?")).strip()
print("Your name has 'Silva'?: {}".format('silva' in name.lower()))

#02option
name = str(input('\n\nDigite o seu nome: ')).strip()
if name.upper().find('SILVA') > -1:
    print('Você tem Silva no nome!')
else:
    print('Você não tem Silva no nome!')
    
#03option - isolando a palavra silva de silvanete
n = str(input('\n\nWhats your complet name?: ')).strip().lower().split()
print("Your name has 'Silva'?: {}".format('silva' in n))