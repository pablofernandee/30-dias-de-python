string_1='Thirty'
print(string_1)
string_2='Days'
print(string_2)
string_3='Of'
print(string_3)
string_4='Python'
print(string_4)
formated_string=format(string_1,string_2,string_3,string_4)
print(formated_string)

string1_1='Coding'
print(string1_1)
string2_1='For'
print(string2_1)
string3_1='All'
print(string3_1)
formated_string2_1=str.format(string1_1,string2_1,string3_1)
print(formated_string2_1)

name_company='Coding for all'
print(name_company)

print(len(name_company))

mayuscula=name_company.upper()
print(mayuscula)
minuscula=mayuscula.lower()
print(minuscula)

usarcapitalizado="Coding For All".capitalize()
usartitle=usarcapitalizado.title()
usarswapcase=usartitle.swapcase()

cut='Coding for all'.split()
for word in cut:
 print(word[0])

verificacion="Coding For All".index()
print(verificacion)

replace1="Coding For All".replace("Coding","Python")
print(replace1)

replace2=replace1.replace("All","Everyone")
print(replace2)


dividircoding="Coding For All".split()
print(dividircoding)

companies="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
separation_comas=companies.split(',')['Facebook', 'Google',' Microsoft', 'Apple', 'IBM', 'Oracle',' Amazon' ]

frase='coding for all'
palabra0=frase[0]
print(palabra0)

frase='coding for all'
ultima_palabra=frase[13]
print(ultima_palabra)

frase='coding for all'
palabra10=frase[10]
print(palabra10)

phrase='python for all'
acronimo=phrase[0,7,11]
print(acronimo)

phrase1='coding for all'
acronimo1=phrase1[0,7,11]

frase='coding for all'
positionofc=frase.index('c')
print(positionofc)


frase='coding for all'
positionoff=frase.index('f')
print(positionoff)

print(frase.rfind('l'))

frassse='You cannot end a sentence with because because because is a conjunction'
print(frassse.index('because'))

print(frassse.rindex('because'))

print(frassse.split())

print(frassse.index('because'))

print(frassse.split())

cortar='coding for all'
print(cortar.startswith('coding'))

print(cortar.endswith('coding'))

print(cortar.replace(' ',''))


buscar_true='30DaysOfPython'
print(buscar_true.isidentifier())

buscartrue='thirty_days_of_python'
print(buscartrue.isidentifier())

list=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
quitarespacio='#'.join(list)
print(quitarespacio)















  







