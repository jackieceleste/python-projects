import random


player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
	print(f"Your score: {player_wins}. Computer score: {computer_wins}")
	random_number = random.randint(1, 3)
	if random_number == 1:
		computer = "rock"
	if random_number == 2:
		computer = "paper"
	if random_number == 3:
		computer = "scissors"
	player = input("Rock, paper, or scissors?\n").lower()
	if computer == player:
		print(f"You both picked {player}. Play again?")
	elif computer == "rock":
		if player == "paper":
			print (f"The computer picked {computer} and you picked {player}. You win!")
			player_wins += 1
		elif player == "scissors":
			print (f"The computer picked {computer} and you picked {player}. The computer wins!")
			computer_wins += 1
	elif computer == "paper":
		if player == "rock":
			print(f"The computer picked {computer} and you picked {player}. The computer wins!")
			computer_wins += 1
		elif player == "scissors":
			print(f"The computer picked {computer} and you picked {player}. You win!")
			player_wins += 1
	elif computer == "scissors":
		if player == "rock":
			print(f"The computer picked {computer} and you picked {player}. You win!")
			player_wins += 1
		elif player == "paper":
			print(f"The computer picked {computer} and you picked {player}. The computer wins!")
			computer_wins += 1
	else:
		print("Something went wrong. Play again?")
print(f"FINAL SCORE: Your score: {player_wins}. Computer score: {computer_wins}")
if player_wins > computer_wins:
	print("You win!")
else:
	print("The computer wins.")


#python3 rock_paper_scissors.py

