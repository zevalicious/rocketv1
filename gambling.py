import random
startyen = 3
while startyen > 5000 or startyen < 1000:
    startyen = int(input('enter amount of yuan that you are playing with total (integers only)'))
    if startyen > 5000 or startyen < 1000:
        print("please only bring 1-5k, this isnt the place for big betters or brokies!!")
again = 'yes'
bet = 9999999
ans = 'var'
while again == 'yes' and startyen > 0:
    while bet > startyen:
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
    dictnum = {1:'ichi', 2:'ni', 3:'san', 4:'shi', 5:'go', 6:'roku'}
    print(f'the numbers were {dictnum[dieone]} and {dictnum[dietwo]}!')
    print(f'you now have {startyen} yuan')
    again = input('do you want to go again? if so, type "yes"')
    ans = 'var'
    if bet > startyen:
        again = 'no'
    else:
        bet = 99999999

if bet > startyen:
    print(f'you no longer have enough to bet! you finished with {startyen} yuan!')
