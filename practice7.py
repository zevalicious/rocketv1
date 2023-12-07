import random
integers=[]
for i in range(13):
    integers.append(random.randint(-10000000,10000000))
cubes=[]
for i in range(17):
    integers.append(i**3)
names = ['tod', 'jane', 'amy', 'sophia', 'mellissa', 'elizebeth']
lastfive = integers[-5:]
intcopy = integers[:]
intcopy.sort()
lowfive=intcopy[:5]

print(intcopy[])
