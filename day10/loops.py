numbers=range(11)
for number in numbers:
    operation='#'*number
    print(operation)


p=[10,9,8,7,6,5,4,3,2,1,0]
for numbe in p:
    y='#'*numbe
    print(y)

h=[0,1,2,3,4,5,6,7]
for num in h:
    o='#'*num
    print(o)


for nu in range(8):
    e=('#'*nu)
    print(e)

l=range(11)
for n in l:
    u=n*n
    print(u)



string=['Python', 'Numpy','Pandas','Django', 'Flask']
for iterator in string:
    print(iterator)

for i in range(101):
    if(i%2)==0:
        continue
    print(i)


for t in range(101):
    if (i%2)!=0:
        continue
    print(t)


suma = 0
for n in range(101):
    suma = suma + n

print(suma)

suma2=0
suma1=0
for r in range(101):
    if r%2!=0:
        continue
    print(suma1)
    suma1=suma1+r
for p in range(101):
    if p%2==0:
        continue
    print(suma2)
    suma2=suma2+p
    



