player=0
import random
while player != "bettor" and player != "house":
    player=(input("do you want to play as the house or the bettor?"))
    if player=='house':
        initialcup=int(input(
            '''which cup should the inital ball be placed under?
            (ball can be under 1 2 or 3)'''))
        movestrings=input(
            '''enter a 8 total letter string of letters
a b and c to move the cup's position)''')
    def cupfinder(initialcup, movestring):
        cuplace = [0,0,0]
        cuplace[initialcup - 1] = 1
        for movestring in movestrings:
            if movestring == 'a':
                cuplace = [cuplace[1], cuplace[0], cuplace[2]]
            if movestring == 'b':
                cuplace = [cuplace[2], cuplace[1], cuplace[0]]
            if movestring == 'c':
                cuplace = [cuplace[0], cuplace[2], cuplace[1]]
        cupnumber = 1
        for cup in cuplace:
            if cup == 1:
                return cupnumber
            cupnumber += 1

    print("the ball is under", cupfinder(initialcup, movestrings))
    if player=='bettor':
        print("n")
    else:
        print("please pick either 'house' or 'bettor'")
