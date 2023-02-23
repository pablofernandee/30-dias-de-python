empty_tuple=tuple()

hermanos=('blanca','carmen','felix')
print(hermanos)

brotherandsister=('marina','carlota','danniela')
print(brotherandsister)

siblins=hermanos+brotherandsister
print(siblins)

nummero_hermanos=len(siblins)
print(nummero_hermanos)
padreymadre=('elena','ruben')


family_members=siblins+padreymadre
print(family_members)

first,second,third,fourth,fifth,sixth,*rest=family_members

fathermother=print(*rest)
print(fathermother)
siblin=print(first,second,third,fourth,fifth,sixth)
print(siblins)

fruits='banana','pera','manzana'
vegetable='lechuga','tomate','apio'
animal_products='carne','pescado','huevo'
food_stuff_tp=fruits+vegetable+animal_products
print(food_stuff_tp)

food_stuff_lt=food_stuff_tp
listfood_stuff_It=list(food_stuff_lt)

print(listfood_stuff_It)

middleoflist=listfood_stuff_It[4:5]
print(middleoflist)
threeitems=listfood_stuff_It[0:3]
print(threeitems)
threelastitem=listfood_stuff_It[0:-3]
print(threelastitem)


del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

comprobarestonia='Estonia' in nordic_countries
print(comprobarestonia)

comprobariceland='iceland' in nordic_countries
print(comprobariceland)




