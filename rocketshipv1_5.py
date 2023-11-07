#zevical, 11/2/2023
#rocketship1.py
#very cool rocket text drawing thingy
#not copyrighted !!

#downward pattern after rocket ends and at top of rocket
jetfuel = '''     /**\\
    //**\\\\
   ///**\\\\\\
  ////**\\\\\\\\
 /////**\\\\\\\\\\'''

jetfuel = ("/"*1)+("**")+("\\"*2)

def jetfuel():
    print((" "*5)+("/"*1)+("**")+("\\"*1))
    print((" "*4)+("/"*2)+("**")+("\\"*2))
    print((" "*3)+("/"*3)+("**")+("\\"*3))
    print((" "*2)+("/"*4)+("**")+("\\"*4))
    print((" "*1)+("/"*5)+("**")+("\\"*5))


def upjetbody():
    print(('|')+("."*2)+("/\\"*1)+(".."*2)+("/\\"*1)+("."*2)+("|"))
    print(("|")+("."*1)+("/\\"*2)+(".."*1)+("/\\"*2)+("."*1)+("|"))
    print(("|")+("."*0)+("/\\"*3)+(".."*0)+("/\\"*3)+("."*0)+("|"))
def downjetbody():
    print(("|")+("."*0)+("\\/"*3)+(".."*0)+("\\/"*3)+("."*0)+("|"))
    print(("|")+("."*1)+("\\/"*2)+(".."*1)+("\\/"*2)+("."*1)+("|"))
    print(("|")+("."*2)+("\\/"*1)+(".."*2)+("\\/"*1)+("."*2)+("|"))

def split():
    print(("+")+("=*"*6)+("+"))
jetfuel()
split()
upjetbody()
downjetbody()
split()
downjetbody()
upjetbody()
split()
jetfuel()
      

