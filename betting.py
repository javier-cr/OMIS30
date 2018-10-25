

number_of_players = input('How many players will be playing? ')

ListOfBets = []   #Create list in which bets will appear
ListOfBets.insert(0,0) # Assign dealer in position 0, $0 to start off with

current_player = 1   #Establish starting position

for i in range (0,int(number_of_players)): #Start with dealer (0) and go until number of entered players
        print("\nHi Player " + str(current_player))
        bet = int(input('What is your bet? '))    #Take bet
        ListOfBets.insert(current_player,bet) # Add bet to list of bets
        current_player+=1

#Diagnostic data, remove when finished
print("\nList of bets list: " + str(ListOfBets))
print("Current player: " + str(current_player))
print("Number of players: " + str(number_of_players))
print("Iteration number of loop: " + str(i))