empty_list=list()
print(empty_list)

list=['futbol','playstation','xerez','portatil','penycom']
print(list)
print(len(list))

firts_item=list[0]
print(firts_item)
midlle_item=list[2]
print(midlle_item)
last_item=list[4]
print(last_item)

mix_data_types=['pablo','16','176','casadojaja','calle batalla de jerez']
print(mix_data_types)

companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(companies)

print(len(companies))

firts_companie=companies[0]
print(firts_companie)
middle_companie=companies[3]
print(middle_companie)
last_companie=companies[6]
print(last_companie)

companies[0]='instagram'
print(companies)

companies.append('tiktok')
print(companies)

companies[0]=companies[0].upper()
print(companies)

companieshastag='#; '
integers=companies+companieshastag
print(integers)

does_exit='Apple'in companies
print(does_exit)

companies.sort()
print(companies)

companies.sort(reverse=True)
print(companies)

companie=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
threefirtscompanies=companie[0:3]
print(threefirtscompanies)

threelastcompanies=companie[0:-3]
print(threelastcompanies)

midlle_compani=companie[3:4]
print(midlle_compani)

removefirtscompany=companie.remove('Facebook')
print(removefirtscompany)

removemiddlecompani=companie.remove('Apple')
print(removemiddlecompani)

removelastcompanie=companie.pop()
print(removelastcompanie)

removeallcompanie= companie.clear()
print(removeallcompanie)

del companies

#mirarlo de borra lista y preguntar lo de las diferentes listas que he puesto
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joinfrontyback=front_end+back_end
print(joinfrontyback)

copiar_lista=joinfrontyback.copy()
print(copiar_lista)

full_stack=copiar_lista
print(full_stack)

meteritem=full_stack.extend('python','SQL')
print(meteritem)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ordenar=ages.sort()
print(ordenar)

encontraminymax=ordenar[0,1,9]
print(encontraminymax)

añadirunoydos=ordenar.insert(19,26)
print(añadirunoydos)














