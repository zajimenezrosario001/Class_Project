#!/usr/bin/env python3
import random 

	
#Function for choosing selection to continue the game
def choice_1():
	print("#1.....#2....")
	choice = input("Choose: ")
	if choice == "1":
		choice_2()
	elif choice == "2":
		#Random death generator for game
		if random.random() < 0.2:
			print("You fall to your death. Game over.")
		else:
			print("You move to the next location etc.")
			choice_3()
	else:
		print("Invalid choice. Try again.")
		choice_1()
