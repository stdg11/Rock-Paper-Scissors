import random

human = input("Enter your choice (rock/paper/scissors): ");
human = human.lower();
while (player!="rock" and player!="paper" and player!="scissors"):
    player = input("%s is not valid. Please re-enter your choice (rock/paper/scissors)" % player);
    player = player.lower();

