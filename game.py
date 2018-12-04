import random
import time
import numpy as np

def offer():
    sum_of_values = sum(combo.values())
    banker_offer = round((sum_of_values/len(combo)),0)
    return banker_offer

def decision(): 
    user_choice = input('What is your choice? Deal or No Deal? Enter\
 y for Deal or n for No Deal.')

    if user_choice == 'y':
        print ('Great! You win $' + str(offer()) + '!')
        play_again = input('Would you like to play again? Enter\
        y for yes or n for no.')
        if play_again == 'y'
            #return to begining 
        elif play_again == 'n'
        exit

        # Restart game
    elif user_choice == 'n':
        print("stupid")
        # Okay, please select 6 more cases
        # Banker offer after 6 more case chosesn
        #repeat this whole if statement

cases_remaining = [] # all cases left for user to pick
cases_picked = [] # all cases that user has already picked

priceLeft = [] # not yet in use
selected = 0 # not yet in use
selectedPrice = 0 # not yet in use

briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,\
14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24 ,25, 26]

listPrice = [0.01, 1.00, 5.00, 10.00, 25.00, 50.00, 75.00,\
100.00, 200.00, 300.00, 400.00, 500.00, 750.00,  \
1000.00, 5000.00, 10000.00, 25000.00, 50000.00, 75000.00,\
100000.00, 200000.00, 300000.00, 400000.00, 500000.00,\
750000.00, 1000000.00]

# shuffle case $ values, not case #'s
random.shuffle(listPrice) 
# creates dictionary with briefcases, listprices
combo = dict(zip(briefcases, listPrice)) 

print(combo) #testing
print(combo.keys()) #testing

# Keep running game while run_game = True. If we want to end the game,
# we set run_game = False.
keep_running = True
while keep_running:
    
    # INTRO - user picks their personal case
    print('Welcome to Deal or No Deal!\nYou may choose a case numbered 1-26.')
    user_case_num = input('\nWhich case would you like to select to be yours?\
 Case #')
    user_case_val = combo[int(user_case_num)] # find right key in dict
    combo.pop(int(user_case_num)) # remove user case from dict
    cases_this_round = 6 # how many cases they'll open this round. start at 6

    print('\nGreat! You have selected your case.\nNow, select ' +\
    str(cases_this_round) + ' cases to open this round.')
    
    # Ask user which cases to open
    cases_opened = {} # make dict of cases opened
    for i in range(1, cases_this_round+1):
        current_case_num = input('Which case should be Case #' + str(i) + '? Case \
        #')
        current_case_val = combo[int(current_case_num)] # find case $ value
        cases_opened[int(current_case_num)] = [current_case_val] # add to new dict
        combo.pop(int(current_case_num)) # remove chosen case from cases left (combo)
        if i == cases_this_round+1:
            cases_this_round -= 1 # user will open 1 less case next time
        else:
            pass


    # Show user values of cases they opened
    print('\nYour personal case is Case #' + str(user_case_num) + ". Let's \
open the cases you picked.\nThe cases you picked had the following values \
inside of them: ")

    for num, val in cases_opened.items():
        print ('Case #' + str(num) + ' had $' + str(val) + ' inside.')


    # Banker calls - CHRIS


    print("The Banker's offer is $" + str(offer())) # prints out banker's offer

    decision()
    # if deal_choice == 'deal':
    #     print('You win ' + banker_offer + ' dollars in prize money!')
    #     play_again = input("Would you like to play again?  (y/n)")
    #     if play_again == 'y':
    #         continue
    #     elif deal_choice == 'quit':
    #         exit
    #     elif play_again == 'n':
    #         exit
    # elif deal_choice == 'no deal':
    #     print('No deal! We will proceed to the next round!')
    #     #help please



        

    keep_running = False # end game?
    