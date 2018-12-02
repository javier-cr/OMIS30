# FROM CHRIS:
import random

class dealOrNoDeal():
    briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,\
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24 ,25, 26]
    listPrice = [0.01, 1.00, 5.00, 10.00, 25.00, 50.00, 100.00,\
    200.00, 300.00, 400.00, 500.00, 750.00, 1000.00, 5000.00,  \
    1000.00, 5,000.00, 10,000.00, 25000.00, 50000.00, 75000.00,\
    100000.00, 200000.00, 300000.00, 400000.00, 500000.00,\
    750000.00, 1000000.00]
    briefcaseWithValue = []
    priceLeft = []
    selected = 0
    selectedPrice = 0
    
    def assignValue(self):
        self.priceLeft = sorted(self.listPrice)
        random.shuffle(self.briefcases)
        self.briefcaseWithValue = dict(zip(self.briefcases, self.listPrice))

    



    
    def finalCase(self):
        print("You have case number " + cases_Remaining +" and your original case number of "+ user_Case + " left.")
        user_final_choice= int(input("Which case number would you like to pick? " + user_Case + " or " + cases_Remaining " ?"))
        print("You have chosen case number " + user_final_choice + ".")
        print("You win " + self.briefcaseWithValue[self.user_final_choice] + " dollars!")
        print("You have reached the end of the game. Thanks for playing!")
    