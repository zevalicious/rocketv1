import random
guessnum = 0
x = 1.1
valuerange = [int(input(
"enter the begining of a range of numbers (ie. '1')")), int(input(
    "enter the end of a range of numbers(ie. '100')"))]
    
answer = random.randint((valuerange[0]), (valuerange[1]))

guesses = int(input("enter how many guesses needed to guess within the given range"))

while x != answer and guesses != guessnum:
    x = int(input("enter an answer"))
    if x>answer:
        print("your input is greater than the real answer")
    elif x<answer:
        print("your input is less than the real answer")
    guessnum +=1
if x == answer:
    print(f"you won!! it took {guessnum} tries, the answer was {answer}")
else:
    print("you lost")
