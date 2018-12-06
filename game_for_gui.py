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

def do_calculation(number1, number2): #from flask tutorial, remove later
    return number1 + number2