
ans=2
shape=(input('''Imput your variables for:generallized quadrilateral, rectangle, triangle, parallelagram, or trapazoid to calculate area'''))
while shape.lower.contains != "gen" or shape.lower.contains != "quad" or shape.lower.contains != "rect" or shape.lower.contains != "sqa" or shape.lower.contains != "par":

if "gen" in shape.lower() or "quad" in shape.lower():
    print('''The area of a quadrilateral is calculated by separating the quadrilateral into two triangles split using the diagonal of the quadrilateral.''')
    
    while True:
        diagonal = float(input("Enter diagonal of the quadrilateral: "))
        height1 = float(input("Enter height of triangle 1: "))
        height2 = float(input("Enter height of triangle 2: "))
        
        if diagonal > 0 and height1 > 0 and height2 > 0:
            area = 0.5 * diagonal * (height1 + height2)
            print(f"The area of the generalized quadrilateral with a diagonal of {diagonal} is {area}")
            break  # Break out of the loop if valid inputs are provided
        else:
            print("Values must be positive real numbers. Please enter valid inputs.")


if "rect" or "par" or "squ" in shape.lower():
    
    while True:
        height=float(input("enter height or altitude"))
        base=float(input("enter base"))
        
        if height>0 and base>0:
            print("the volume of the rectangle with a diagonal of", diagonal, "is", (1/2)*diagonal*(height1+height2))
        else:
        print("values must be a positive real numbers")
        height=(input("enter new height"))
        base=(input("enter new base"))
