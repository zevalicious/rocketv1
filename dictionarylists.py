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
ana = {"name":'ana', 'height':64, 'age':16, 'hair':'brown', 'gender':'female'}
print(ana)
print(ana['age'])
ana['home'] = '124 apple ave'
for key in ana.keys():
    print(f"ana's {key} is {ana[key]}.")
ana.update({'job':'walmart employee'})
ana.get('job')
print(ana.get('spouse', "I don't know that info"))
ana.pop('job')
#removes job xd
