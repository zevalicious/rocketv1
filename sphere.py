PIE=3.1415926535897932846

diameter=float(input("enter diameter of the sphere"))
if diameter>0:
    print("the diameter of the sphere with a diameter of", diameter, "is"
          (4/3)*(PIE)*((.5*diameter)**3))
if diameter<0:
    print("diameter cannot be negative")
