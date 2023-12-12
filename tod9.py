import random

x = "1"

answer = [random.randint(0, 9), random.randint(0, 9),
          random.randint(0, 9), random.randint(0, 9)]

while x != "yes":
    x = input("enter your 4 number answer")
    x.split()
    for i in range(0,3):
        if x[i] == answer[i]:
            print(f"{x[i]} is green")
        for x[i] in answer[:]:
            print(f'{x[i]} is yellow')
        else:
            print("red")
        if x[0] == answer[0] and x[1] == answer[1] and x[2] == answer[2] and x[3] == answer[3] and x[4] == answer[4]:
            x = "yes"
    
if x == answer:
    print(f"you won!! it took {guessnum} tries, the answer was {answer}")
else:
    print("you lost")
