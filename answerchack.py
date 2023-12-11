import random
valuerange = (input("enter range of numbers(ie. '1,100')"))
answer = random.randint(valuerange)
while x != answer:
    x = int(input("enter an answer"))
    if x>answer:
        print("your input is greater than the real answer")
    elif x<answer:
        print("your input is less than the real answer")

print("your answer is correct!")
