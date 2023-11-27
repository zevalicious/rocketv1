#zevical, 11/27/2023
#basketballwinner.py
#user input's basketball scores, thingy puts out winner and team points.
#not copyrighted !!


#first team variables
ateamname=(input("enter team name"))
athreepointer=int(input("enter team's # of three pointers"))
atwopointer=int(input("enter team's # of two pointers"))
aonepointer=int(input("enter team's # of free throws"))
#second team variables
bteamname=(input("enter second team's name"))
bthreepointer=int(input("enter second team's # of three pointers"))
btwopointer=int(input("enter second team's # of two pointers"))
bonepointer=int(input("enter second team's # of free throws"))
ateamtotal=((athreepointer*3) + (atwopointer*2) + (aonepointer))
bteamtotal=((bthreepointer*3) + (btwopointer*2) + (bonepointer))
if (ateamtotal>bteamtotal):
    print(ateamname, "won with a total of", ateamtotal, "and", bteamname,
          "lost with a total of", bteamtotal)
          
if (bteamtotal>ateamtotal):
    print(bteamname, "won with a total of", bteamtotal, "and", ateamname,
          "lost with a total of", ateamtotal)
