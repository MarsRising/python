import random
#Deck of cards/player and dealer hand
J= 10
Q= 10
K= 10
A= 1 or 11
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]

money=100

while True
  print("Player's Total Money:", money, "\n1)Bet?", "\n2)CashOut", "\n3)Quit\n"
  decision=input('Enter Your Choice')
        if decision=='1':
          first_card=random.choice(deck)
          print("Player's first card is:", first_card)
          dealer_card=random.choice(deck)
          print("Dealer's face up card is:", dealer_card)
          second_card=random.choice(deck)
          print("Player's second card is:", second_card)
          dealer_hidden=random.choice(deck)
          your_hand=first_card+second_card
          print("Your hand is", your_hand, ". The dealer is showing", dealer_card, ".\n")
          signal=input("Would you like Stay or Hit?\n 1) Stay\n2)Hit")
          if signal=='1':
            third_card=random.choice(deck)
            your_hand=your_hand+third_card
            print("\nYou drew", third_card)
            if your_hand>21:
              print("\nYou BUSTED!")
              money= money-15
              continue
            elif your_hand<=21:
              print("\nYour hand is now", your_hand, "\n1) Stay   or   2) Hit")
player= []
dealer= []
#Deal the cards
random.choice(deck)
#calculate the total of each hand

#Check for winner

#game loop
