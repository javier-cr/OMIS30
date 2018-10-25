#Created by: Tanner Suard
#Purpose: Project 2 for OMIS30, create a blackjack simulator
#Date: October 24, 2018

import random
import itertools
from sys import platform as _platform
import os


# ****************************************************************************
# BEGIN FUNCTIONS FOR GENERAL USE (below)...
# ****************************************************************************

#define a function for a deck of cards with 6 decks within it
def deck_of_cards():
    suits= ("Hearts","Diamonds","Clubs","Spades")
    cardvalues= ["A","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    deck=[]
    for cardvalue in cardvalues:
        for suit in suits:
            deck.append(cardvalue + " of " + suit) 
    deck_1= []      
    for i in deck:  
        b=6*[i] #make loop for 6 decks to combine into one large deck
        #create correct number of cards with each card type in it's own list
        deck_1.extend([b]) 
    #flatten all lists of cards to make one big list with all cards
    deck_of_six=list(itertools.chain.from_iterable(deck_1)) 
    random.shuffle(deck_of_six) #shuffle deck
    return deck_of_six

#create a deck that can be popped and used repeatedly until runs out of cards.
deck_of_six=deck_of_cards()   
cardvalues= ["A","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
 #            0   1   2   3   4   5   6   7   8    9   10      11      12

#Function for providing integer value for cards dealt
def value_of_card(card):
    if card[:1] in ('J','Q','K','1'):
        return int(10)
    elif card[:1] in ('2','3','4','5','6','7','8','9'):
        return int(card[:1])
    elif card[:1] == 'A':
        print ("\n"+ str(card))
        num = input("Would you like this Ace to be worth 1 or 11? ")
        while num !='1' or num !='11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Would you like this Ace to be worth 1 or 11? ")

#give a new card and remove card from original list                 
def new_card(deck_of_six):   
    return deck_of_six.pop(0)      


# allow us to change text style
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# ****************************************************************************
# BEGIN USER-FACING CODE (below)
# ****************************************************************************


# Detect OS to clear terminal window
if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    os.system('clear') # clear terminal
elif _platform == "win32" or _platform == "win64":
    os.system('cls') # clear cmd or ps
else:
    pass # or do nothing


# INTRO: Welcome to Blackjack!  
print(color.BOLD + color.BLUE + "Welcome to Blackjack!\n" + color.GREEN + "  \
  .... Created by Tanner, Chris, & Javi.\n" + color.END + color.BOLD + "\nNow,\
 let's get started.\n" + color.END)

# COLLECT BETS
bet = int(input("What is your bet? ")) # Take in bet input    

# START THE GAME
print(color.BOLD + "\nThanks for that information. You have been dealt\
 a hand. " + color.END + "\n")
 
# DEAL CARDS
doLoop = True
while doLoop:
    #Create a player's hand  (maybe loop to create mulitple players??)
    card_1= new_card(deck_of_six)
    card_2= new_card(deck_of_six)
    print("For your first hand, you were dealt a " + color.BOLD + card_1 +\
     color.END + " and a " + color.BOLD + card_2 + "." + color.END, end=" ")
    #turn String of card1 into int. Check for ace and 10
    value_1= value_of_card(card_1) 
    value_2= value_of_card(card_2)
    
    global value_hand
    value_hand= value_1 + value_2 # PROBLEMATIC LINE
    print ("\n@174 Value Hand is: " + str(value_hand) + "\n")
    print("Your total hand value is " + color.BOLD + str(value_hand) + "."+\
     color.END + "\n")


    #Create Dealer's hand
    dealer_card_1= new_card(deck_of_six)
    dealer_card_2= new_card(deck_of_six)
    dealer_value_1= value_of_card(dealer_card_1)
    dealer_value_2= value_of_card(dealer_card_2)
    dealer_value_hand= dealer_value_1 + dealer_value_2
    print("The Dealer deals himself two cards, one card face up and one card\
 face down.", end=" ")
    print("The face up card is a " + color.BOLD + dealer_card_1 + "." +\
     color.END + "\n")


    #Blackjack results if player has blackjack
    if value_hand == 21:
        print("Congratulations! You got a Blackjack!")
        print("The Dealer now reveals his second card which is a "\
         + dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
        if dealer_value_hand== 21 and value_hand== 21:
            print("You and the Dealer both have Blackjack so you push and tie!")
            bet = bet # bet stays the same, okay to remove this line too
            play_again = input("Would you like to play another hand? Or you can\
             type exit to leave\n")
            if play_again == "exit":
                break
            else: 
                pass
        else: 
            print("You win!") # player wins a Blackjack
            bet = bet + (bet * 1.5)
            play_again = input("Would you like to play another hand? Or you can\
             type exit to leave\n")
            if play_again == "exit":
                break
            else: 
                pass


    else:
        while value_hand < 21:
            user_input= input("Would you like to hit or stand? \n")
            if user_input== "hit" or user_input=="Hit":
                card_3= new_card(deck_of_six) # we get a fresh, random card from the deck
                value_3= value_of_card(card_3) 
                value_hand += value_3 # this always line always breaks
                print("\nYou are dealt a " + card_3 + " for a total of "\
                 + str(value_hand) + ".")

                if value_hand > 21:
                    print("\nYou busted; therefore, you lose this hand.")
                    bet = 0
                else:
                    print("The Dealer reveals his face down card to be a "\
                    + dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
            
                    while dealer_value_hand < 17:
                        print("The Dealer must hit.")
                        dealer_card_3= new_card(deck_of_six)
                        dealer_value_3= value_of_card(dealer_card_3)
                        dealer_value_hand+= dealer_value_3
                        print("The Dealer drew a " + dealer_card_3 + " for a total of "\
                        + str(dealer_value_hand)+ ".")
                        if dealer_value_hand > 21 and value_hand <= 21:
                            print("The Dealer busted... You win!")
                        elif dealer_value_hand < 21 and dealer_value_hand > value_hand:
                            print("The Dealer has a higher hand than you. You lose!")
                        else:
                            continue

                    if dealer_value_hand == value_hand:
                        print("There is a push. Player and Dealer tie.")
                    elif dealer_value_hand < value_hand:
                        print("You have a higher hand than the Dealer. You win!")
                    else:
                        print("The Dealer has a higher hand than you. You lose!")

            elif user_input== "stand" or user_input== "Stand":
                print("The Dealer reveals his face down card to be a " +\
                dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
                
                if dealer_value_hand < 17:
                    print("The Dealer must hit.")
                    dealer_card_3= new_card(deck_of_six)
                    dealer_value_3= value_of_card(dealer_card_3)
                    dealer_value_hand+= dealer_value_3
                    print("The Dealer drew a " + dealer_card_3 + " for a total of " + str(dealer_value_hand)+ ".")
                    
                    if dealer_value_hand > 21 and value_hand <= 21:
                        print("The Dealer busted... You win!")
                    elif dealer_value_hand < 21 and dealer_value_hand > value_hand:
                        print("The Dealer has a higher hand than you. You lose!")
                    else:
                        continue
                
                elif dealer_value_hand == value_hand:
                    print("There is a push. Player and Dealer tie.")
                elif dealer_value_hand < value_hand:
                    print("You have a higher hand than the Dealer. You win!")
                else:
                    print("The Dealer has a higher hand than you. You lose!")
                break
        play_again= input("Would you like to play another hand? Or you can type exit to leave\n")
        if play_again == "exit":
            break
        else: 
            pass