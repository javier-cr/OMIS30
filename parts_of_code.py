#Created by: Tanner Suard, Javier Ramirez, and Chris Martin
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
            deck.append(cardvalue + " of " + suit)   #Append suits and values to create cards
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
    if card[:1] in ("J","Q","K","1"):
        return int(10)    #Assign a value of 10 to 10's and face cards
    elif card[:1] in ("2","3","4","5","6","7","8","9"):
        return int(card[:1])     #Assign value of number cards equal to the number
    elif card[:1] == "A":
        print ("\n"+ str(card))
        num = input("Would you like this Ace to be worth 1 or 11? ")    #Give option for value of Ace
        while num !="1" or num !="11":
            if num == "1":
                return int(1)     #Add one to hand value if 1 is chosen 
            elif num == "11":
                return int(11)     #Add 11 to hand value if qq is chosen
            else:
                num = input("Would you like this Ace to be worth 1 or 11? ")

#give a new card and remove card from original list                 
def new_card(deck_of_six):   
    return deck_of_six.pop(0)      


# allow us to change text style
class color:
   PURPLE = "\033[95m"
   CYAN = "\033[96m"
   DARKCYAN = "\033[36m"
   BLUE = "\033[94m"
   GREEN = "\033[92m"
   YELLOW = "\033[93m"
   RED = "\033[91m"
   BOLD = "\033[1m"
   UNDERLINE = "\033[4m"
   END = "\033[0m"


# ****************************************************************************
# BEGIN USER-FACING CODE (below)
# ****************************************************************************


# Detect OS to clear terminal window
if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    os.system("clear") # clear terminal
elif _platform == "win32" or _platform == "win64":
    os.system("cls") # clear cmd or ps
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
#doLoop = True
dont_Break1 = True
dont_Break2 = True
while dont_Break1 and dont_Break2:
    #Create a player's hand  (maybe loop to create mulitple players??)
    card_1= new_card(deck_of_six)
    card_2= new_card(deck_of_six)
    print("For your first hand, you were dealt a " + color.BOLD + card_1 +\
     color.END + " and a " + color.BOLD + card_2 + "." + color.END, end=" ")
    #turn String of card1 into int. Check for ace and 10
    value_1= value_of_card(card_1) 
    value_2= value_of_card(card_2)
    
    global value_hand
    value_hand= value_1 + value_2
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
        print(color.GREEN+ "Congratulations! You got a Blackjack!" + color.END)
        print("The Dealer now reveals his second card which is a "\
         + dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
         # Establish rules if user and dealer tie at a blackjack
        if dealer_value_hand== 21 and value_hand== 21:
            print(color.YELLOW + "You and the Dealer both have Blackjack so you push and tie!" + color.END)
            bet = bet # bet stays the same, okay to remove this line too
            play_again = input("Would you like to play another hand? Or you can\
             type exit to leave\n")
            if play_again == "exit":   #Allow user to exit program
                break
            else: 
                pass
        else: 
            print(color.GREEN + "You win!" + color.END) # player wins a Blackjack
            bet = bet + (bet * 1.5)
            play_again = input("Would you like to play another hand? Or you can\
             type exit to leave\n")
            if play_again == "exit":      #Allow user to exit program
                break
            else: 
                pass

    
    else: # if amount DOESN'T equal 21...
        while dont_Break2: # = True...
            if value_hand < 21:
                user_Choice = input("Would you like to hit or stand? Enter hit or stand. ")
                
                if user_Choice == "hit" or user_Choice == "Hit":
                    deciding_Card = new_card(deck_of_six) # we get a new card from the combined deck
                    deciding_Card_Value = value_of_card(deciding_Card)
                    value_hand += deciding_Card_Value    #Add value of card to total hand value
                    print("\nYou were dealt a " + deciding_Card + " for a total of "\
                 + str(value_hand) + ".")
                    
                    if value_hand > 21:
                        print (color.RED + "Your hand is over 21. You busted!" + color.END)
                        bet = 0    #Lose the money you bet
                        play_again = input("Would you like to play another hand? Or you can type exit to leave\n")
                        if play_again == "exit":
                            dont_Break1 = False  # exit out of main loop
                            dont_Break2 = False  # exit out of secondary loop
                            break
                        else: 
                            pass
                    elif value_hand == 21:    #Rules for if user gets a blackjack
                        print (color.GREEN + "You got a Blackjack, you win!" + color.END)
                        bet = bet + (bet * 1.5)
                        play_again = input("Would you like to play another hand? Or you can type exit to leave\n")
                        if play_again == "exit":
                            dont_Break1 = False
                            dont_Break2 = False
                            break
                        else: pass
            
                elif user_Choice == "stand" or user_Choice == "Stand":    #Rules for if user stands instead of hitting
                    while True: 
                        if dealer_value_hand < 17:
                            print("The dealer's hand equals less than 17, so they must hit.", end=" ")
                            
                            deciding_Card_Dealer = new_card(deck_of_six) # we get a new card from the combined deck
                            deciding_Card_Dealer_Value = value_of_card(deciding_Card_Dealer)
                            dealer_value_hand += deciding_Card_Dealer_Value
                            print("The dealer was dealt a " + deciding_Card_Dealer + " for a total of " +\
                         str(dealer_value_hand) + ".")
                        
                        
                        elif dealer_value_hand >16 and dealer_value_hand <21:   
                            #If dealer passes his/her hit limit, but does not bust
                            #if value is 1-21 
                            if dealer_value_hand > value_hand:
                                print(color.RED + "You lose. The dealer wins!\n" + color.END)
                                bet = 0
                                play_again = input("Would you like to play another hand? Or you can type exit to leave\n")
                                if play_again == "exit":
                                    dont_Break1 = False
                                    dont_Break2 = False
                                    break
                                else: pass
                            elif dealer_value_hand < value_hand: 
                                #Both dealer and user are done below 21 and user has higher score
                                print(color.GREEN + "You win! Collect your money!" + color.END)
                                if value_hand == 21:
                                    bet = bet + (bet * 1.5)  #Win by black jack gets 1.5 times the bet limit
                                elif value_hand < 21:
                                    bet = bet + bet
                                play_again = input("Would you like to play another hand? Or you can type exit to leave\n")
                                if play_again == "exit":
                                    dont_Break1 = False
                                    dont_Break2 = False
                                    break
                                else: pass
                            elif dealer_value_hand == value_hand:
                                print(color.YELLOW + "You and the dealer tie resulting in a push! Collect the money you bet" + color.END)
                                #User and dealer are below 21 but tie
                                bet = bet   #User gets money back
                                play_again = input("Would you like to play another hand? Or you can type exit to leave\n")
                                if play_again == "exit":
                                    dont_Break1 = False
                                    dont_Break2 = False
                                    break
                                else: pass
                        elif dealer_value_hand > 21:
                            print(color.GREEN + "The dealer busted! You Win" + color.END)
                            if value_hand == 21:
                                    bet = bet + (bet * 1.5)
                            elif value_hand < 21:
                                    bet = bet + bet
                            play_again = input("Would you like to play another hand? Or you can type exit to leave\n")
                            if play_again == "exit":
                                dont_Break1 = False
                                dont_Break2 = False
                                break
                            else: pass
        print (color.PURPLE + "You ended with $" + str(bet) + "." + color.END)