import random
startyen = 0
while startyen > 5000 or startyen < 1000:
    startyen = int(input('enter amount of yuan that you are playing with total (integers only)'))
    if startyen > 5000 or startyen < 1000:
        print("please only bring 1-5k, this isnt the place for big betters or brokies!!")
again = 'yes'
bet = 9999999
ans = 'var'
while again == 'yes':
    while bet >= startyen:
        bet = int(input('how much would you like to bet? (integers only)'))
        if bet > startyen:
            print('please bet less than your total amount')
    dieone = random.randint(1,6)
    dietwo = random.randint(1,6)
    totalcount = dieone + dietwo
    print('you are betting on if the dice roll is either odd or even')
    while ans != 'even' and ans != 'odd':
        ans = input('type "even" or "odd" based on what you the dice roll is')
    if (totalcount%2) == 0 and ans == "even":
        print('you won')
        startyen += bet
    elif (totalcount%2) != 0 and ans == "odd":
        print('you won')
        startyen += bet
    else:
        print('you lost')
        startyen -= bet
    print(f'the number was {totalcount}!')
    print(f'you now have {startyen} yuan')
    again = input('do you want to go again? if so, type "yes"')
    ans = 'var'
