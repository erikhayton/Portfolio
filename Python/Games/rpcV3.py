import random
# more specified imput
# from random import randint
human_wins=0
computer_wins=0
winning_score=2

while human_wins < winning_score and computer_wins < winning_score:
    print(f"Puny Human Score: {human_wins} Computer Score: {computer_wins}")
    # shorter
    human = input("Puny human: Input rock, paper, or scissors! ").lower()
    if human =="quit" or human == "q":
        break
    rand_num = random.randint(0,2)
    # more specified
    # rand_num = randint(0,2)

    # computer 
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print("computer played: " + computer)

    # human
    if human == computer:
        print("Draw")
    elif human == "rock" and computer == "scissors":
        print("puny human wins")
        human_wins += 1
    elif human == "paper" and computer == "rock":
        print("puny human wins")
        human_wins += 1
    elif human == "scissors" and computer == "paper":
        print("puny human wins")
        human_wins += 1
    else:
        print("computer wins")
        computer_wins += 1
print(
"*\n"
"*\n"
"*")
print(f"FINAL SCORES: Puny Human: {human_wins} Computer: {computer_wins}")
print(
"*\n"
"*\n"
"*")
if human_wins > computer_wins:
    print("Congrats Dumbass! Now you're on Technology's Hit List!")
elif human_wins == computer_wins:
    print("You'll never amount to anything...Quitter!")
else:
    print("You have pleased the Google overlords...Loser!")
print(
"\n"
)
