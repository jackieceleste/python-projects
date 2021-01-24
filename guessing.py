import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low
# BONUS - let player play again if they want!

playing = True
while playing == True:
	guess = int(input("Guess a number between 1 and 10: "))
	while guess != random_number:
		if guess > random_number:
			guess = int(input("Too high, try again! "))
		elif guess < random_number:
			guess = int(input("Too low, try again! "))
	print("You guessed it! You won!")
	if input("Do you want to play again? (y/n) ") == "n":
		playing = False
