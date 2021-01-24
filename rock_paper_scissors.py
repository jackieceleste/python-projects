import random
random_number = random.randint(1,3)
if random_number == 1:
	computer = "rock"
if random_number == 2:
	computer = "paper"
if random_number == 3:
	computer = "scissors"

while True:
	player = input("Rock, paper, or scissors?\n").lower()
	if computer == player:
		print(f"You both picked {player}. Play again?")
	elif computer == "rock":
		if player == "paper":
			print (f"The computer picked {computer} and you picked {player}. You win!")
		elif player == "scissors":
			print (f"The computer picked {computer} and you picked {player}. The computer wins!")
	elif computer == "paper":
		if player == "rock":
			print(f"The computer picked {computer} and you picked {player}. The computer wins!")
		elif player == "scissors":
			print(f"The computer picked {computer} and you picked {player}. You win!")
	elif computer == "scissors":
		if player == "rock":
			print(f"The computer picked {computer} and you picked {player}. You win!")
		elif player == "paper":
			print(f"The computer picked {computer} and you picked {player}. The computer wins!")
	else:
		print("Something went wrong. Play again?")
	again = input("Play again? (y/n) ")
	if again == "n":
		break


