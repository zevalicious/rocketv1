import random
valuerange = [(input(
    "enter the begining of a range of numbers (ie. '1')")), (input(
        "enter the end of a range of numbers(ie. '100')"))]
    
answer = random.randint(int(valuerange[0]), int(valuerange[1]))
x = 1.1
while x != answer:
    x = int(input("enter an answer"))
    if x>answer:
        print("your input is greater than the real answer")
    elif x<answer:
        print("your input is less than the real answer")

print("your answer is correct!")
