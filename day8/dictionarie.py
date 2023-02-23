dog={'fits_name':'mckeen',
     'age':12,
     'color':'black',
    'breed':'pitbull',
    'legs':'4',
    'age':'four months'}
print(dog)


student = {'firtsname':'jimenez',
         'last_name':'cararsco',
         'gender':'boy',
         'marital status':'single',
         'skills':['negotation skills','playfootbal very well'],
         'country':'spain',
         'city':'merbella',
         'adress':{'street':'calle romero vargas',
                   'zipcode':'15435'}}
print(student)

longitud=len(student)
print(longitud)


skilllista=student['skills']
valueskill=print(student['skills'])
print(valueskill)

tiposkill=type(valueskill)
print(tiposkill)

comprobarlista=(tiposkill==list)
print(comprobarlista)

student['skills'].append('Pensamiento crítico','gran Capacidad de aprendizaje')
print(student)

keys=student.values()
print(keys)

convertirenlista=student.items()
print(convertirenlista)

removelasitem=student.popitem()
print(removelasitem)
 
del dog



