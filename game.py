import random
import time

briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,\
14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24 ,25, 26]

listPrice = [0.01, 1.00, 5.00, 10.00, 25.00, 50.00, 75.00,\
100.00, 200.00, 300.00, 400.00, 500.00, 750.00,  \
1000.00, 5000.00, 10000.00, 25000.00, 50000.00, 75000.00,\
100000.00, 200000.00, 300000.00, 400000.00, 500000.00,\
750000.00, 1000000.00]

cases_opened = {} # make dict of cases opened
user_case_num = None
user_case_val = None
cases_this_round = 6 # how many cases they'll open this round. start at 6

random.shuffle(listPrice) # shuffle case values, not nums
combo = dict(zip(briefcases, listPrice)) # create dict with case nums, vals


def intro():
    # WELCOME
    print('Welcome to Deal or No Deal!\nYou may choose a case numbered 1-26.')


def pick_user_case():
    global user_case_num, user_case_val
    user_case_num = input('\nWhich case would you like to select to be yours?\
 Case #')
    if user_case_num.isnumeric() and int(user_case_num) > 0 and int(user_case_num) < 27:
        user_case_val = combo[int(user_case_num)] # find right key in dict
        combo.pop(int(user_case_num)) # remove user case from dict
        print('\nGreat! You have selected your case.\n')
        return user_case_num, user_case_val
    else:
        print('\nThat is not a valid number! Please enter a number 1 - 26!')
        pick_user_case()


def pick_cases(cases_this_round):
    print('Your options are: ', combo.keys())

    for i in range(1, cases_this_round+1):
        current_case_num = input('Which case should be Case #' + str(i) + \
' to eliminate? Case #')
        if current_case_num.isnumeric() and int(current_case_num) > 0 and int(current_case_num) < 27:
            current_case_val = combo[int(current_case_num)] # find case $ value
            cases_opened[int(current_case_num)] = [current_case_val] # add to new dict
            combo.pop(int(current_case_num)) # remove chosen case from cases left (combo)
            if i == cases_this_round+1:
                cases_this_round -= 1 # user will open 1 less case next time
            else:
                pass
        else:
            print('\nThat is not a valid input! Please enter a number 1-26 from the remaining cases!\n')
            pick_cases(cases_this_round)
    
    
def show_cases():
    print('\nYour personal case is Case #' + str(user_case_num) + ". Let's \
open the cases you picked.\nThe cases you picked had the following values \
inside of them:\n")

    for num, val in cases_opened.items():
        print ('Case #' + str(num) + ' had $' + str(val) + ' inside.')
    #offer() - moved this to end and keep going


def decision(): 
    print("\nThe Banker's offer is $" + str(offer()) + "\n") # banker offer
    
    user_choice = input('What is your choice? Deal or No Deal? Enter "deal" \
for Deal or "no deal" for No Deal. \n')
    
    if user_choice == "deal" or user_choice == "Deal":
        print ('\nCongratulations, you won $' + str(offer()) + '! Thank you \
for playing.\n')
        quit() # player wins, ends game

    elif user_choice == "no deal" or user_choice == "No Deal":
        print("\nNO DEAL! We will proceed to the next round!\n")
        keep_going()
    else:
        print('That is not a valid answer! Please enter "deal" or "no deal". ')
        decision()


def offer():
    sum_of_values = sum(combo.values())
    banker_offer = round((sum_of_values/len(combo)),0)
    return banker_offer


def finalCase(): #left for tomorrow
    global cases_this_round
    print('finalCase is in motion.')

    if len(combo) == 1:
        
        final_choice = input('You have made it to the last round. You must \
either open your personal case or the only one left.\
Your personal case is ' + str(user_case_num) + ". \
The only case left is " + str(combo.keys())+ ". \
Enter 'mine' to keep you case or 'switch' to choose the final case.\n")
        if final_choice == 'mine' or 'Mine':
            print ("You picked " + str(user_case_num)+ "! You win $" + str(user_case_val) + ". \
            Thanks for playing!")
        elif final_choice == 'switch' or 'Switch':
            print ("You picked case " + str(combo.keys()) + "! You win $" + str(combo.items()) + ". \
             Thanks for playing!")
        else:
            print('\nThat is not a valid input! Please enter "mine" or "switch"\n')
            finalCase()
    
    elif cases_this_round <= 1:
        print("Now, you may only pick 1 case at a time.")
        pick_cases(cases_this_round)
        show_cases()
        offer()
        decision()
        
    else: 
        pick_cases(cases_this_round)
        show_cases()
        offer()
        decision()

def keep_going():
    global cases_this_round

    if cases_this_round == 1:
        finalCase()
    #elif len(combo) == 4:
    #    print('...')
    else:
        print('Now, select ' + str(cases_this_round) + ' cases to open this \
round.')
        pick_cases(cases_this_round)
        show_cases()
        offer()
        cases_this_round -= 1
        decision()


intro()
pick_user_case()
pick_cases(cases_this_round)
show_cases()
offer()
cases_this_round -=1
decision()

#keep_going() This is already called within the decision function. No need for this here.