
#zevical, 11/7/2023
#rocketship1.py
#very cool rocket text drawing thingy
#not copyrighted !!

size=8
#size cannot = numbers that lead to text wrapping around the screen (for me its high 40's)

def upjet():
    for i in range(1, size+1):
        print('|'
            + "." * (size-i)
            + "/\\" * (i)
            + ".." * ((size-i))
            + "/\\" * (i)
            + "." * (size-i)
            + "|")
def downjet():
    for i in range(1, size+1):
        print('|'
            + "." * (i-1)
            + "\\/" * ((size-i)+1)
            + ".." * (i-1)
            + "\\/" * ((size-i)+1)
            + "." * (i-1)
            + "|")
def split():
        print(("+")+("=*"* (size*2))+("+"))
#jetfuel issue fixed 
def jetfuel():
    for i in range(1, (size*2)+1):
        print(
            " " * ((size*2)-i)
            + "/" * (i)
            + "**"
            + "\\" * (i))

def diamondbody():
    upjet()
    downjet()
def hourglassbody():
    downjet()
    upjet()
    

#code
jetfuel()
split()
diamondbody()
split()
hourglassbody()
split()
jetfuel()
