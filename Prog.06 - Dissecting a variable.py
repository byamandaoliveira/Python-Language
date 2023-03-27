#Dissecting a variable: 3 modes
#First mode

x = str(input('Digite alguma coisa:'))
print(type(x))
print('É alfabético?', x.isalpha())
print('É Numérico?', x.isnumeric())
print('É alfanumérico?', x.isalnum())
print('Está tudo escrito em minúsculo?', x.isupper())
print('Está tudo escrito em minúsculo?', x.islower())
print('É um número decimal?', x.isdecimal())
print('É um identificador?', x.isidentifier())
print('Pode ser impresso?', x.isprintable())
print('Começa com letras maiúsculas e termina com minúsculas?', x.istitle())
print('É um dígito?', x.isdigit())
print('Contém apenas espaços?', x.isspace())

/////////////////////////////////////////////////////////////////////////////
#Second mode

a = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?:', 'Sim.' if a.isspace() else 'Não.')
print('É um numero?:', 'Sim.' if a.isnumeric() else 'Não.')
print('É um alfabético?:', 'Sim.' if a.isalpha() else 'Não.')
print('É um alfanumérico?:', 'Sim.' if a.isalnum() else 'Não.')
print('Está em maiúsculo?:', 'Sim.' if a.isupper() else 'Não.')
print('Está em minúsculo?: ', 'Sim.' if a.islower() else 'Não.')
print('Está capitalizada?:', 'Sim.' if a.istitle() else 'Não.')

///////////////////////////////////////////////////////////////////////////////////

#third mode

s = input('Escreva algo: ')
print(f' O tipo Primitivo desse valor é: {type(s)}',
      f'\n Só tem espaços? {s.isspace()}',
      f'\n É um Número? {s.isnumeric()}',
      f'\n É alfabético? {s.isalpha()}',
      f'\n É alfanumérico? {s.isalnum()}',
      f'\n Está em Maiusculas? {s.isupper()}',
      f'\n Está em Mínusculas {s.islower()}',
      f'\n Está Capitalizada? {s.istitle()}')