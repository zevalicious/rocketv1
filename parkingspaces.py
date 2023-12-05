totalspot=int(input("enter number of parking spots"))
yesterday=(input("""enter a string where c is a spot occupied by a car
    and . is a spot unocupied (cc...c.c..cc) representing yesterday's occupancy"""))
today=(input("""enter a string where c is a spot occupied by a car
    and . is a spot unocupied (cc...c.c..cc) representing today's occupancy"""))
todayslist=list(today)
yesterdayslist=list(yesterday)


x=0
moredays = []
for i in range(len(yesterdayslist)):
    if yesterdayslist[i].lower() == "c":
        if todayslist[i].lower() == "c":
            x=x+1
            moredays.append(i)



print(x)
print(moredays)

