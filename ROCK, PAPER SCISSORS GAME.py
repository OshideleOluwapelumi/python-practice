print("ROCK, PAPER SCISSORS SHOOT!!")
play1 = input("Your play player 1: ")
play2 = input("Your play player 2: ")
if play1 == "ROCK" and play2 == "ROCK":
    print("TIE!!!!")
elif play1 == "PAPER" and play2 == "PAPER":
    print("TIE!!!!")
elif play1 == "SCISSORS" and play2 == "SCISSORS":
    print("TIE!!!!")
elif play1 == "ROCK" and play2 == "PAPER":
    print("PLAYER 2 WINS!!!")
elif play1 == "PAPER" and play2 == "ROCK":
    print("PLAYER 1 WINS!!!")
elif play1 == "ROCK" and play2 == "SCISSORS":
    print("PLAYER 1 WINS!!!")
elif play1 == "SCISSORS" and play2 == "ROCK":
    print("PLAYER 2 WINS!!!")
elif play1 == "SCISSORS" and play2 == "PAPER":
    print("PLAYER 1 WINS!!!")
elif play1 == "PAPER" and play2 == "SCISSORS":
    print("PLAYER 2 WINS!!!")
