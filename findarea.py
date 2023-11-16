
ans=2
shape=(input('''Imput your variables for:generallized quadrilateral, rectangle, triangle, parallelagram, or trapazoid to calculate area'''))

elif "gen" or "quad" in shape.lower():
    print('''area of a quadrilateral is calculated by seperating the quadrilateral into
    two triangles split using the diagonal of the quadrilateral''')
    diagonal=float(input("enter diagonal of the quadrilateral"))
    height1=float(input("enter height of triangle 1"))
    height2=float(input("enter height of triangle 2"))
    if diagonal>0 and height1>0 and height2>0:
        print("the volume of the generalized quadrilateral with a diagonal of", diagonal, "is", ((1/2) * (diagonal)) * (height1 + height2))
    while diagonal<0 or height1<0 or height2<0:
        print("values must be a positive real numbers")
        height1=(input("enter new height of triangle 1"))
        height2=(input("enter new height of triangle 2"))
        diaginal=(input("enter new length of diagonal"))

elif "rect" or "par" or "squ" in shape.lower():
    height=float(input("enter height or altitude"))
    base=float(input("enter base"))
    if height>0 and base>0:
        print("the volume of the rectangle with a diagonal of", diagonal, "is", (1/2)*diagonal*(height1+height2))
    while height<0 or base<0:
        print("values must be a positive real numbers")
        height=(input("enter new height"))
        base=(input("enter new base"))
