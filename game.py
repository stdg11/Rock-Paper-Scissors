import random

player = input("Enter your choice (rock/paper/scissors): ")
player = player.lower()
while (player!="rock" and player!="paper" and player!="scissors"):
    player = input("%s is not valid. Please re-enter your choice (rock/paper/scissors)" % player)
    player = player.lower()

computer = ['rock','paper','scissors']
computer = random.choice(computer)

if (player == computer):
    print("Draw")
elif (player == "rock"):
    if (computer =="paper"):
        print("Computer Wins!")
    else:
        print("You Win!")
elif (player == "paper"):
    if (computer == "scissors"):
        print("Computer Wins!")
    else:
        print("You Win!")
elif (player == "scissors"):
    if (computer == "rock"):
        print("Computer Wins!")
    else:
        print("You Win!")

print("You chose %s \nComputer picked %s \n Thank you for playing!") % (player, computer)
input("Press any key to exit.")
