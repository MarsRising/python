import random

#game initialized
high_score = 0

#game works
while True:
    print('Current High Score:', high score, \n '1)Roll Dice', \n, '2) Leave Game'\n)
    dice_game=input('Enter your Choice:')
        if dice_game=='1':
            thrown=random.randint(1, 6)
            print('You roll a ...', str(thrown), \n)
            throwntwo=random.randint(1,6)
            print('You roll a ...', str(throwntwo), \n)
            roll= throw+throwtwo
            print('You have rolled a total of:', roll)
                if roll > high_score
                    high_score=roll
                    print(New High Score!)
        elif dice_game=='2':
            quit()
        else:
            print("Unknown Response")
