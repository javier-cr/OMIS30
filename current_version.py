#Created by: Tanner Suard
#Purpose: Project 2 for OMIS30, create a blackjack simulator
#Date: October 24, 2018

import random
import itertools
from sys import platform as _platform
import os


# ****************************************************************************
# BEGIN FUNCTIONS FOR GENERAL USE (below)
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
    if card[0] in cardvalues[9:12+1]: # if card is a 10 or J/Q/K
        return int(10)
    elif card[0] in cardvalues[1:9]: # if card is a # 2 thru 9, inclusive
        return int(card[0])
    elif card[0] == "A": # if card is a Ace
        #create value_hand list with total value of cards. If over 11 with ace in it, 
        # then ace has to be a 1
        if value_hand >= 11:
            return int(1)
        elif value_hand < 11:
            ace_choice = input("You drew an Ace. Would you like to treat the Ace as a 1 or 11? ")
            if ace_choice == '1':
                return int(1)
            elif ace_choice == '11':
                return int(11)
            else:
                return int(999999)
        elif value_hand == 0:
            ace_choice = input("You drew an Ace. Would you like to treat the Ace as a 1 or 11? ")
        else: return int(999999)

        # first card, and we need to keep going. Ask user if 1 or 11
        # not first card, user hand is 11 or less --> ask user if 1 or 11
        # not first card, user hand is 12 or greater --> treat as 1

        
        
        
        
        '''
        if value_hand>11: 
            return int(1)
        else:
            ace_value= input("Would you like to treat the " + str(card) +\
             " as a 1 or 11? \n")
            while ace_value !="1" or ace_value !="11":    #input validation
                if ace_value== "1" or ace_value== "11":
                    return int(ace_value)
                elif ace_value== "one":
                    return int(1)
                elif ace_value== "eleven":
                    return int(11)
                else:
                    ace_value== str(input("Please enter a 1 or 11 as the value\
                     for your " + str(card)+ "? \n"))
    else:
        return int(999999)   
    '''        

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


# COLLECT # OF USERS & VALIDATE
while True: #validate input
    number_of_players = input("How many people are playing? ")
    if number_of_players.isdigit() and int(number_of_players) > 0:
        break
    else:
        continue

# CREATE LIST OF BETS & CURRENT PLAYER TRACKER-var
print(color.BOLD,"\nGot it,", number_of_players, "people will be playing.",\
color.END, "Now, we'll collect bets.\n")
ListOfBets = [] # Create list in which bets will appear
ListOfBets.insert(0,0) # Assign dealer in position 0, $0 to start off with
current_player = 1   # Establish starting position


# COLLECT BETS
# Start with dealer (0) and go until number of entered players
for i in range (0,int(number_of_players)): 
        bet = int(input("Player " + (str(current_player)) + ", what is your\
 bet? ")) # Take in bet input
        ListOfBets.insert(current_player,bet) # Add bet to list of bets
        current_player+=1 # move on to next player        


# START THE GAME
print(color.BOLD + "\nThanks for that information. Each player has been dealt\
 a hand. " + color.END + "We'll start with Player 1.\n")
current_player = 1

#Deal cards if users want to play again
play_again = ""
while play_again!= "exit" or play_again!= "Exit":
    #Create a player's hand  (maybe loop to create mulitple players??)
    card_1= new_card(deck_of_six)
    card_2= new_card(deck_of_six)
    print("For your first hand, you were dealt a " + color.BOLD + card_1 +\
     color.END + " and a " + color.BOLD + card_2 + "." + color.END, end=" ")
    #turn String of card1 into int. Check for ace and 10
    value_1= value_of_card(card_1) 
    value_2= value_of_card(card_2)
    # DEBUG CODE:
    print ("@174 Value 1 is: " + str(value_1) + "\n")
    print ("@175 Value 2 is: " + str(value_2) + "\n")
    
    # END DEBUG CODE
    value_hand= value_1 + value_2 # PROBLEMATIC LINE
    print ("@176 Value Hand is: " + str(value_hand) + "\n")
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
            play_again = input("Would you like to play another hand? Or you can\
             type exit to leave\n")
        else:
            print("You win!")
            play_again = input("Would you like to play another hand? Or you can\
             type exit to leave\n")

    else:
        while value_hand < 21:
            user_input= input("Would you like to hit or stand? \n")
            if user_input== "hit" or user_input=="Hit":
                card_3= new_card(deck_of_six) # we get a fresh, random card from the deck
                value_3= value_of_card(card_3) #
                # DEBUG CODE:
                print ("@217 Value 3 is: " + str(value_3) + "\n")
                print ("@218 Value Hand is: " + str(value_hand) + "\n")
                # END DEBUG CODE

                value_hand += value_3 # this always line always breaks
                print("\nYou are dealt a " + card_3 + " for a total of "\
                 + str(value_hand) + ".")

                if value_hand > 21:
                    print("\nYou busted; therefore, you lose this hand.")
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