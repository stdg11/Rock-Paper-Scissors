import random
playing = True

def computer_choice():
    computer = ['rock','paper','scissors']
    computer = random.choice(computer)
    return computer

def play_hand(player, computer):
    if (player == computer):
        winner = 'draw'
    elif (player == "rock" and computer == "paper") or (player == "paper" and computer == "scissors") or (player == "scissors" and computer == "rock"):
        winner = 'computer'
    else:
        winner = 'player'
    return winner

def play_game():
    playing = True
    while playing:
        player = input("Enter your choice (rock/paper/scissors): ")
        player = player.lower()
        while (player!="rock" and player!="paper" and player!="scissors"):
            player = input("%s is not valid. Please re-enter your choice (rock/paper/scissors)" % player)
            player = player.lower()
        computer = computer_choice()
        winner = play_hand(player, computer)
        if (winner == 'computer'):
            print("\nUnlucky Computer Won")
        elif (winner == 'player'):
            print("\nCongratulations you Won!")
        elif (winner == 'draw'):
            print("\nIt's a Draw")
        else:
            print("\nOops..")
        print("You chose: %s | Computer picked: %s" % (player, computer))
        play_again = input("\nPlay again? (Y/N)")
        if (play_again == 'N' or play_again == 'n'):
            playing = False

print("Let's play Rock, Paper, Scissors!")
play_game()
input("Press any key to exit.")
