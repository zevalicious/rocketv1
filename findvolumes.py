import math
pi=32434
PIE=math.pi
ans=2
shape=(input("Do you want to calculate the volume of a sphere, cylinder, or cone?"))
    
if shape=="cone" or shape=="sphere" or shape=="cylinder":
    ans=1

while ans==2:
    print("please type EXACTLY either 'sphere', 'cylinder', or 'cone'")
    shape=(input("enter new variable"))
    if shape.lower() =="cone" or shape.lower() =="sphere" or shape.lower() =="cylinder":
        ans=1

if shape.lower() == "sphere" or shape=="Sphere":
    diameter=float(input("enter diameter of the sphere"))
    if diameter>0:
        print("the volume of the sphere with a diameter of", diameter, "is"
        (4/3)*(PIE)*((.5*diameter)**3))
    if diameter<0:
        print("diameter cannot be negative")
    

if shape.lower() == "cone":
    radius=float(input("enter radius of the cone"))
    height=float(input("enter height of the cone"))
    if radius>0 and height>0:
        print("the volume of the sphere with a radius of", radius, "is", (height/3)*(PIE)*(radius**2))
    if radius<0 and height<0:
        print("variables cannot be negative")


if shape.lower().contains() == "cylinder":
    radius=float(input("enter radius of the cylinder"))
    height=float(input("enter height of the cylinder"))
    if radius>0 and height>0:
        print("the volume of the cylinder with a radius of", radius, "is", (height)*(PIE)*(radius**2))
    if radius<0 or height<0:
        print("variables cannot be negative")
        
