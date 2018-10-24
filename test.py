

number_of_players = input('How many players will be playing? \n')

ListOfBets = []

current_player = 1

for i in number_of_players:
        print("Hi Player " + str(current_player))
        bet = input('What is your bet?')
        ListOfBets[current_player] = bet
        current_player+=1