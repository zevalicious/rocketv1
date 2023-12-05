import random

squarelist = []
x=0
for i in range(12):
    squarelist.append(i*i)
integers = []
y=0
for i in range(25):
    integers.append(i+1)

colors = ["red", 'blue', 'green', 'purple', 'yellow', 'orange', 'violet', 'white']

people = ['tom', 'jeremy', 'jacob', 'william', 'daniel']
height = []
z=0
for i in range(5):
    height.append(random.randint(60,73))
print(squarelist)
print(height)
print(integers)
for color in colors:
    if color == "yelljow":
        print("pinnaple")
