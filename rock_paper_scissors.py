
player1 = input("Player 1: rock, paper, or scissors?\n").lower()
print("**NO CHEATING**\n" * 30)

player2 = input("Player 2: rock, paper, or scissors?\n").lower()
if player1 == player2:
	print(f"You both picked {player1}. Play again?")
elif player1 == "rock":
	if player2 == "paper":
		print (f"Player 1 picked {player1} and player 2 picked {player2}. Player 2 wins!")
	elif player2 == "scissors":
		print (f"Player 1 picked {player1} and player 2 picked {player2}. Player 1 wins!")
elif player1 == "paper":
	if player2 == "rock":
		print(f"Player 1 picked {player1} and player 2 picked {player2}. Player 1 wins!")
	elif player2 == "scissors":
		print(f"Player 1 picked {player1} and player 2 picked {player2}. Player 2 wins!")
elif player1 == "scissors":
	if player2 == "rock":
		print(f"Player 1 picked {player1} and player 2 picked {player2}. Player 2 wins!")
	elif player2 == "paper":
		print(f"Player 1 picked {player1} and player 2 picked {player2}. Player 1 wins!")
else:
	print("Something went wrong. Play again?")


