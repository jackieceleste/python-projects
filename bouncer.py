#ask for age
age = input("How old are you? ")

if age:
	age = int(age)
	if age >= 21:
		#21+ drink, normal entry
		print("You can enter. Here is your wristband.")
	elif age >= 18:
		#18-20 wristband
		print("You can enter, but can't drink.")
	else:
		# too young, sorry
		print("You are too young to enter.")
else:
	print("Please enter an age.")

