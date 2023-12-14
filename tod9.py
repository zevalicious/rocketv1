import random

x = "1"

answer = [random.randint(0, 9), random.randint(0, 9),
          random.randint(0, 9), random.randint(0, 9)]

while x != "yes":
    x = [int(input("enter your 1st number"
                   )), int(input("""enter your 2nd number"""
                                 )), int(input("enter your 3rd number"
                                               )), int(input("enter your 4th number"))]
    print(x)
    for i in range(4):
        if x[i] == answer[i]:
            print(x[i])
            print(f"{i+1} is green")
        elif x[i] in answer:
            print(x[i])
            print(f'{i+1} is yellow')
        else:
            print(x[i])
            print(f"{i+1} is red")
        print(x)
        if x == answer:
            x = "yes"
    
if x == answer:
    print(f"you won!! it took {guessnum} tries, the answer was {answer}")
else:
    print("you lost")
