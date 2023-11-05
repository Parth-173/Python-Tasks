import random as rd
computer_points = 0
player_points = 0
while True:
    list = ['ROCK','PAPER','SCISSOR']
    computer_choice = rd.choice(list)
    player_choice = input("Enter choice (Rock, Paper, Scissor) : ").upper()
    print("Computer's choice : ",computer_choice,"\nYour choice : ",player_choice)
    if computer_choice == player_choice :
        print(f"Both player selected {computer_choice}.It's a tie")
    elif computer_choice == 'ROCK':
        if player_choice == 'PAPER':
            print(f"{player_choice} covers {computer_choice}. You WIN !")
            player_points +=1
        else:
            print(f"{computer_choice} smashes {player_choice}. You LOSE !")
            computer_points += 1
    elif computer_choice == 'PAPER':
        if player_choice == 'SCISSOR':
            print(f"{player_choice} cuts {computer_choice}. You WIN !")
            player_points +=1
        else:
            print(f"{computer_choice} covers {player_choice}. You LOSE !")
            computer_points += 1
    elif computer_choice == 'SCISSOR':
        if player_choice == 'ROCK':
            print(f"{player_choice} smashes {computer_choice}. You WIN !")
            player_points +=1
        else:
            print(f"{computer_choice} cuts {player_choice}. You LOSE !")
            computer_points += 1
    else:
        print("Enter correct choice : ")
    print("Computer Points : ",computer_points)
    print("Your Points : ",player_points)
