
size=5

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

def jetfuel():
    for i in range(1, size+6):
        print(
            " " * ((size*2)-i)
            + "/" * (i)
            + "**"
            + "\\" * (i))


#code
jetfuel()
split()
upjet()
downjet()
split()
downjet()
upjet()
split()
jetfuel()
