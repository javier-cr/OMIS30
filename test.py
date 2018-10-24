

number_of_players = input('How many players will be playing? \n')

ListOfBets = []

current_player = 1

for i in range(1, len(int((number_of_players)+1))):
        print("Hi Player " + current_player)
        bet = input('What is your bet?')
        ListOfBets[current_player] = bet
        current_player+=1