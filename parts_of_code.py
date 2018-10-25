def value_of_card(card):
    #turn strings of values into integers for cards that equal 10 for the game.
    if card[0] in cardvalues[9:13]:
        return int(10)
    #turn strings of values into integers for strait numbers 2 thru 9 for the game.
    elif card[0] in cardvalues[1:9]:
        return int(card[0])
    #turn strings of values into integres for Ace. Allow player to use ace as an 11 or 1.
    elif card[0] == "A":
        if value_hand>11:   #create value_hand list with total value of cards and if over 11 with ace in it, then ace has to be a 1
            return int(1)
        else:
            ace_value= input("Would you like to treat the " + str(card) + " as a 1 or 11? \n")
            while ace_value !="1" or ace_value !="11":    #input validation
                if ace_value== "1" or ace_value== "11":
                    return int(ace_value)
                elif ace_value== "one":
                    return int(1)
                elif ace_value== "eleven":
                    return int(11)
                else:
                    ace_value== str(input("Please enter a 1 or 11 as the value for your " + str(card)+ "? \n"))
                 

#give a new card and remove card from original list                 
def new_card(deck_of_six):   
    return deck_of_six.pop(0)     











#Deal cards if users want to play again
play_again = ""
while play_again!= "exit" or play_again!= "Exit":
    #Create a player's hand  (maybe loop to create mulitple players??)
    card_1= new_card(deck_of_six)
    card_2= new_card(deck_of_six)
    print("You have received a " + card_1 + " and a " + card_2 + ".")
    value_1= value_of_card(card_1) #turn String of card1 into int #Check for ace and 10
    value_2= value_of_card(card_2)
    value_hand= value_1 + value_2
    print("Your total hand value is " + str(value_hand) + ".")


    #Create Dealer's hand
    dealer_card_1= new_card(deck_of_six)
    dealer_card_2= new_card(deck_of_six)
    dealer_value_1= value_of_card(dealer_card_1)
    dealer_value_2= value_of_card(dealer_card_2)
    dealer_value_hand= dealer_value_1 + dealer_value_2
    print("The Dealer deals himself two cards. One face up and one face down.")
    print("The face up card is a " + dealer_card_1 + ".")

    #Blackjack results if player has blackjack
    if value_hand == 21:
        print("Congratulations! You got a Blackjack!")
        print("The Dealer now reveals his second card which is a " + dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
        if dealer_value_hand== 21 and value_hand== 21:
            print("You and the Dealer both have Blackjack so you push and tie!")
            play_again = input("Would you like to play another hand? Or you can type exit to leave\n")
        else:
            print("You win!")
            play_again = input("Would you like to play another hand? Or you can type exit to leave\n")
    
    else:  
        while value_hand < 21:
            user_input= input("Would you like to hit or stand? \n")
            if user_input== "hit" or user_input=="Hit":
                card_3= new_card(deck_of_six)
                value_3= value_of_card(card_3)
                value_hand += value_3
                print("You are dealt a " + card_3 + " for a total of " + str(value_hand) + ".")
            
                if value_hand > 21:
                    print("You busted; therefore, you lose this hand.")
                    
                
                else:
                    print("The Dealer reveals his face down card to be a " + dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
                    while dealer_value_hand < 17:
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
                    if dealer_value_hand == value_hand:
                        print("There is a push. Player and Dealer tie.")
                        
                    elif dealer_value_hand < value_hand:
                        print("You have a higher hand than the Dealer. You win!")
                        
                    else:
                        print("The Dealer has a higher hand than you. You lose!")
                    
            elif user_input== "stand" or user_input== "Stand":
                print("The Dealer reveals his face down card to be a " + dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
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