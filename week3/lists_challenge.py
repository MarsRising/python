import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D","7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand=[]

while diamonds:
    player=input("Please enter to pick a card, or Q then enter to quit:")
    if player.upper()=="Q":
        break
    else:
        user_card=random.choice(diamonds)
        diamonds.remove(user_card)
        hand.append(user_card)
    print("Your hand: ", str(hand))
    print("Remaining Cards: ", str(diamonds), "\n")
if not diamonds:
    print("There are no more cards to pick.")