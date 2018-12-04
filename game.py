import random
import time
import numpy as np
#
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

# SHUFFLE the briefcases
combo = [] # list of lists [case number, case $$ value]
random.shuffle(listPrice) # shuffle only case values (not case #'s)
combo = [[x, y] for x, y in zip(briefcases, listPrice)] # combine into 1 list
#print(combo)


def finalCase(self):
    print("You have case number " + cases_remaining +" and your original case number of "+ user_case + " left.")
    user_final_choice= int(input("Which case number would you like to pick? " + user_case + " or " + cases_remaining + " ?"))
    print("You have chosen case number " + user_final_choice + ".")
    print("You win " + self.briefcaseWithValue[self.user_final_choice] + " dollars!")
    print("You have reached the end of the game. Thanks for playing!")

# Keep running game while run_game = True. If we want to end the game,
# we set run_game = False.
keep_running = True
while keep_running:
    
    # INTRO
    print('Welcome to Deal or No Deal!\nYou may choose a case numbered 1-26.')
    user_case = input('\nWhich case would you like to select to be yours? Case #')
    cases_remaining = combo.pop((int(user_case))-1) # remove from combo (both)

    #cases_remaining.remove(user_case) # remove from available cases
    #cases_picked.append(user_case) # add to cases chosen
    cases_this_round = 6 # how many cases they'll open this round. start at 6

    print('\nGreat! You have selected your case.\nNow, select ' +\
    str(cases_this_round) + ' cases to open this round.')

    # Ask user which cases to open
    cases_opened = []
    for i in range(1, cases_this_round+1):
        current_num = input('Which case should be Case #' + str(i) + '? Case #')
        cases_opened.append(current_num)
        
        if i == cases_this_round+1:
            cases_this_round -= 1 # so that user will open 1 less case next time
        else:
            pass

    # Show user values of cases they opened
    print('\nYour personal case is Case #' + str(user_case) + ". Let's open the \
    cases you picked.\nThe cases you picked had the following values \
    inside of them: ")
    
    for j in range (0, len(cases_opened)):
        time.sleep(2) #delay for 2 seconds
        print ('Case #' + (str(cases_opened[j]) + ' had X amount inside of it.'))

    # Banker calls - CHRIS


    banker_offer = np.mean(cases_remaining)
    print("The banker is calling! Let's hear what he has to offer!")
    print('.')
    print('.')
    print('.')
    time.sleep(2)
    print("The Banker's offer is", banker_offer, 'dollars')
    deal_choice = input('Will you accept the offer?    (deal/no deal/quit)   ')
    if deal_choice == 'deal':
        print('You win ' + banker_offer + ' dollars in prize money!')
        play_again = input("Would you like to play again?  (y/n)")
        if play_again == 'y':
            continue
        elif deal_choice == 'quit':
            exit
        elif play_again == 'n':
            exit
    elif deal_choice == 'no deal':
        print('No deal! We will proceed to the next round!')
        #help please



        

    keep_running = False # end game?
    