#Created by: Tanner Suard
#Purpose: Project 2 for OMIS30, create a blackjack simulator
#Date: October 24, 2018

#import libraries
import random
import collections
import itertools
#deck of cards with 6 decks within it
suits= ("H","D","C","S")
cardvalues= ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
deck=[]
for cardvalue in cardvalues:
    for suit in suits:
        deck.append(cardvalue + suit) 
deck_1= []      
for i in deck:  
    b=6*[i]        #make loop for number of decks you want in one large deck
    deck_1.extend([b]) #create correct number of cards but each card type in own list
deck_of_cards=list(itertools.chain.from_iterable(deck_1)) #flatten all lists of cards to make one big list with all cards


#Create a list of drawn cards
#ending_cards= []

#Welcome user Tanner
print("Welcome to Blackjack! Your cards have been dealt.")
#Deal cards
user_hand=[]
dealer_hand=[]
for deal in range(0,1):
    #Shuffle the deck
    random.shuffle(deck_of_cards)

    #put first two cards into hand
    user_hand = deck_of_cards[0:2]
    dealer_hand= deck_of_cards[2:4]

    #print user hand and dealer's second card (1st card is hidden)
    print("Your starting hand is " + str(user_hand))
    print("The dealer has a "+ str(dealer_hand[1]) + " showing.")

#Ask user to hit or stand
user_answer= input("What would you like to do? Hit or Stand? \n")
if user_answer== "Hit" or user_answer=="hit":
    user_hand.append(deck_of_cards[4])
    print("You drew a " + str(deck_of_cards[4]))
    print("Your hand now contains " + str(user_hand))

elif user_answer== "Stand" or user_answer== "stand":
    print("You have chosen to stand.")
    user_hand=user_hand #probably not needed

else:
    print("Please restart and enter a valid response (Hit or Stand).")


#split up user's hand into integers and add them together. If over 21, then bust. If 21, then win. If under 21, dealer's turn(must stay if under 17).







    #put cards dealt into new list
    #ending_cards.append(deck_of_cards[x])
    #print adjusted tuple
    #print(ending_cards) 