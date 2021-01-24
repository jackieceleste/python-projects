
#version 1
#answer = input("Hey, how's it going? ").lower()
# while answer != "stop copying me":
# 	print(answer)
# 	answer = input().lower()
# print("UGH FINE YOU WIN")

#version 2
answer = input("Hey, how's it going? ").lower()
while answer != "stop copying me":
	answer = input(f"{answer} ")
print("UGH FINE YOU WIN")