
ans=2
shape=(input('''Imput:generallized quadrilateral, rectangle, triangle, parallelagram, or trapazoid to calculate area'''))
while "rect" not in shape.lower() and "par" not in shape.lower() and "squ" not in shape.lower(
    ) and "gen" not in shape.lower() and "quad" not in shape.lower():
    print("Input invalid, please input new shape to calculate area")
    shape=(input('''Imput:generallized quadrilateral, rectangle, triangle, parallelagram, or trapazoid to calculate area'''))
    
if "gen" in shape.lower() or "quad" in shape.lower():
    print('''The area of a quadrilateral is calculated by separating the quadrilateral into two triangles split using the diagonal of the quadrilateral.''')
    
    while True:
        print("enter numbers!")
        diagonal = float(input("Enter diagonal of the quadrilateral: "))
        height1 = float(input("Enter height of triangle 1: "))
        height2 = float(input("Enter height of triangle 2: "))
        if diagonal > 0 or height1 > 0 or height2 > 0:
            area = 0.5 * diagonal * (height1 + height2)
            print(f"The area of the generalized quadrilateral with a diagonal of {diagonal} is {area}")
            break
        else:
            print("Values must be positive real numbers. Please enter valid inputs.")


if "rect" in shape.lower() or "par" in shape.lower() or "squ" in shape.lower():
    
    while True:
        height=float(input("enter height or altitude"))
        base=float(input("enter base"))
        
        if height>0 and base>0:
            print("the area of the rectangle, parrallelagram, or square", "is", (base*height))
        else:
            print("values must be a positive real numbers")
            height=float(input("enter new height"))
            base=float(input("enter new base"))

