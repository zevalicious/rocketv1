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
bailey = {"name":'bailey', 'height':69, 'age':16, 'hair':'brown', 'gender':'male'}
print(bailey)
print(bailey['age'])
bailey['home'] = '124 apple ave'
for key in bailey.keys():
    print(f"bailey's {key} is {bailey[key]}.")
bailey.update({'job':'walmart employee', "friends":['tod', 'will', 'john']})
bailey.get('job')
print(bailey.get('spouse',"I don't know that info"))
#removes job xd
bailey.pop('job')
bailey['job'] = 'professional gambler'

#import random

#squarelist = []
#x=0
#for i in range(12):
#    squarelist.append(i*i)
#integers = []
#y=0
#for i in range(25):
#    integers.append(i+1)

#colors = ["red", 'blue', 'green', 'purple', 'yellow', 'orange', 'violet', 'white']

#people = ['tom', 'jeremy', 'jacob', 'william', 'daniel']
#height = []
#z=0
#for i in range(5):
#    height.append(random.randint(60,73))
#print(squarelist)
#print(height)
#print(integers)
#for color in colors:
#    if color == "yelljow":
#        print("pinnaple")
