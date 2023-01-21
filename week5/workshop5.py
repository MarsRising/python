import random

def guess_random_number(tries, start, stop):
    secret=random.randint(start, stop+1)
    while tries !=0:
        print("\n"+str(tries), "number of tries remaining.")
        guess=input("Guess a number between "+ str(start) + " and "+ str(stop) + ": ")
        if int(secret)==int(guess):
            print("Success! Congrats you guessed the number with", str(tries), "tries remaining.")
            break
        if int(guess)<int(secret):
            print("Guess Higher!")
        if int(guess)>int(secret):
            print("Guess Lower!")
        tries-=1
        if int(tries)==0:
            print("You have failed. Na na na boo boo, stick your head in doo doo")
            break

# #Test Driver Code#
# guess_random_number(5, 0, 10)

#Task 2 is not a linear function
def guess_random_num_linear(tries, start, stop):
    secret=random.randint(start, stop)
    print('The number for the program to guess is:', str(secret))
    for x in range (start, stop):
        if x==secret:
            print("Programming is guessing....", x)
            print("Program guessed the number correctly:", x)
            return x
        else:
            print ("Programming is guessing....", x)
        tries-=1
        if tries==0:
            print("The system failed to guess number in available tries.")
            break
        else:
            print("Number of tries left:", tries)


#Test Driver Code#
#guess_random_num_linear(5, 0, 10)

def guess_random_num_binary(tries, start, stop):
    secret=random.randint(start, stop)
    print('Random number to guess is:', str(secret))
    lower_bound=start
    upper_bound=stop

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2

        if pivot==secret:
            print("Found it!", secret)
            return pivot
        if pivot > secret:
            print("Guessing Lower!")
            upper_bound=pivot
        else:
            print("Guessing Higher!")
            lower_bound=pivot
        tries-=1
        if tries==0:
            print("You're program failed to find the number.")
            break

#Test Driver Code#
guess_random_num_binary(20, 0, 1000)