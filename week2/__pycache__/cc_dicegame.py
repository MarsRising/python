import random

#game initialized
high_score = 0

#game works
while True:
    print('Current High Score:', high_score, '\n1)Roll Dice\n' + '2)Leave Game')
    dice_game=input('Enter your Choice:')
    if dice_game=='1':
        thrown=random.randint(1, 6)
        print('\nYou roll a ...', str(thrown))
        throwntwo=random.randint(1,6)
        print('You roll a ...', str(throwntwo))
        roll= thrown+throwntwo
        print('\nYou have rolled a total of:', roll)
        if roll > high_score:
            high_score=roll
            print('\nNew High Score!\n')
    elif dice_game=='2':
        quit()
    else:
        print("Unknown Response")