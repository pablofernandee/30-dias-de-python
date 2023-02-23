age=input('Enter your age:')
if age>= 18:
 print('You are old enough to learn to drive')
 if age<=18:
  h=(18-age)
print('you need {h} more years to learn to drive')

myage=16
yourage=input('Enter your age:')

if myage==yourage:
     print('you are the same age than me ')

else:
   print('you were born at the same age than me')

if yourage>myage:
     m=yourage-myage
     print('you are {m} years older than me') 
else:
   o=yourage-myage
   print('you were born {o} before me')

if yourage<myage:
     q='you are'
     l=myage-yourage
     k='smaller than me'
     print('you are {l} smaller than me')
else:
   p=myage-yourage
   print('you were born {p} after than me')



numberone=input('Enter a number:')
numbertwo=input('Enter a number:')
if numberone>numbertwo:
   print('{numbertwo} is less than {numberone}')
else:
   print('{numberone} is greather than {numbertwo}')

if numberone<numbertwo:
   print('{numberone} is less than {numbertwo}')
else:
   print('{numbertwo} is greather than {numberone}')




mark=input('Enter mark:')
if mark==0<=49:
   print(mark)
else:
   print('F')

if mark>=50<=59:
   print(mark)
else:
   print('D')

if mark>=60<=69:
   print(mark)
else:
   print('C')

if mark>=70<=89:
   print(mark)
else:
   print('B')

if mark>=80<=100:
   print(mark)
else:
   print('A')
  


season=input('Enter month:')

if season=='September'or 'October' or 'November':
   print(season)
else:
   print('The season is Autumn')

if season=='December'or 'January' or 'February':
   print(season)
else:
   print('The season is Winter')

if season=='March'or 'April' or 'May':
   print(season)
else:
   print('The season is Spring')

if season=='June'or 'July' or 'August':
   print(season)
else:
   print('The season is Summer')




fruits = ['banana', 'orange', 'mango', 'lemon']
fruta=input('Enter a fruit:')
if fruta in fruits:
   print(fruta)
else:
   print('That fruit already exist in the list')

if fruta not in fruits:
   print('fruta are not in the list')
elif fruta not in fruits:
   fruits.append(fruta)
else:
   print(fruits)








   