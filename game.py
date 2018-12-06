import random
import time
import numpy as np

briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,\
14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24 ,25, 26]

listPrice = [0.01, 1.00, 5.00, 10.00, 25.00, 50.00, 75.00,\
100.00, 200.00, 300.00, 400.00, 500.00, 750.00,  \
1000.00, 5000.00, 10000.00, 25000.00, 50000.00, 75000.00,\
100000.00, 200000.00, 300000.00, 400000.00, 500000.00,\
750000.00, 1000000.00]

cases_opened = {} # make dict of cases opened

# shuffle case $ values, not case #'s
random.shuffle(listPrice) 
# creates dictionary with briefcases, listprices
combo = dict(zip(briefcases, listPrice)) 

cases_this_round = 6 # how many cases they'll open this round. start at 6



def pick_cases(cases_this_round):
    print('Your options are: ', combo.keys())

    for i in range(1, cases_this_round+1):
        current_case_num = input('Which case should be Case #' + str(i) + '? Case #')
        current_case_val = combo[int(current_case_num)] # find case $ value
        cases_opened[int(current_case_num)] = [current_case_val] # add to new dict
        combo.pop(int(current_case_num)) # remove chosen case from cases left (combo)
        if i == cases_this_round+1:
            cases_this_round -= 1 # user will open 1 less case next time
        else:
            pass
   
    # while len(combo) != 1:
    #     decision()
    # else:
    #     lastValue()
    #     finalCase()
    




def show_cases():
    print('\nYour personal case is Case #' + str(user_case_num) + ". Let's \
open the cases you picked.\nThe cases you picked had the following values \
inside of them: ")

    for num, val in cases_opened.items():
        print ('Case #' + str(num) + ' had $' + str(val) + ' inside.')
    offer()


def lastValue():
    for num, val in cases_opened.items():
        print ('Case #' + str(num) + ' had $' + str(val) + ' inside.')







def offer():
    sum_of_values = sum(combo.values())
    banker_offer = round((sum_of_values/len(combo)),0)
    return banker_offer





def decision(): 
    print("\nThe Banker's offer is $" + str(offer()) + "\n") # prints out banker's offer
    
    user_choice = input('What is your choice? Deal or No Deal? Enter "deal" for Deal \
    or "no deal" for No Deal. \n')
    
    if user_choice == "deal" or user_choice == "Deal":
        print ('Great! You win $' + str(offer()) + '!')
        exit # player wins, ends game

    elif user_choice == "no deal" or user_choice == "No Deal":
        print("NO DEAL! We will proceed to the next round!")
        keep_going()
        # pick_cases(cases_this_round)
        # Okay, please select 6 more cases
        # Banker offer after 6 more case chosesn
        #repeat this whole if statement







def finalCase():
    print("The remaining case is ")

def keep_going() :
    print('Now, select ' + str(cases_this_round) + ' case to open this round.')

    pick_cases(cases_this_round)
    show_cases()
    decision()
    print("just finished keep_going")




# Keep running game while run_game = True. If we want to end the game,
# we set run_game = False.
# keep_running = True
# while cases_this_round > 0:
# for x in range(cases_this_round)  :
# INTRO - user picks their personal case
print('Welcome to Deal or No Deal!\nYou may choose a case numbered 1-26.')
user_case_num = input('\nWhich case would you like to select to be yours?\
Case #')
user_case_val = combo[int(user_case_num)] # find right key in dict
combo.pop(int(user_case_num)) # remove user case from dict

print('\nGreat! You have selected your case.\n')
print("back in while loop")
cases_this_round -= 1
keep_going()

# decision()
# keep_running = False # end game?