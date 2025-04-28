#!/usr/bin/env python3

import random
import sys

def start_game():
	# This function starts the game and introduces the player to the story.
	print("You wake up in a dark forest with no memory of how you got here. Your goal is to survive and find a way out.\nWrite 'save' to save the game or 'end' if you want to quit.")
	choice_1()

def save_game(current_choice):
	# This function saves the current game state to a file.
	save = open("save.txt","w")
	save.write(str(current_choice))
	save.close()

def check_action(choice, level):
	# This function checks if the player wants to save or end the game.
	if choice.lower() == "save":
		save_game(level)
		print("Game saved!")
		return
	if choice.lower() == "end":
		print("See you next time!")
		sys.exit(0)
			
# The next functions represent different choices the player can make in the game.
# Each function corresponds to a different part of the story and leads to further choices.
def choice_1():
	print("\n1. Follow a faint trail.\n2. Climb a tree to get a better view.")
	choice = input("Choose: ")
	choice = choice.strip(" ")
	check_action(choice, 1)
	if choice == "1":
		choice_2()
	elif choice == "2":
		if random.random() < 0.2:
			print("You slip and fall to your death. Game over.")
		else:
			print("You see a river in the distance and decide to head that way.")
			choice_3()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_1()
		
def choice_2():
	print("\n1. Keep following the trail.\n2. Go off the path into the trees.")
	choice = input("Choose: ")
	check_action(choice, 2)
	if choice == "1":
		choice_3()
	elif choice == "2":
		if random.random() < 0.3:
			print("You walk into a trap and die. Game over.")
		else:
			print("You find a cave entrance.")
			choice_4()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_2()
		
def choice_3():
	print("\n1. Follow the river downstream.\n2. Try to catch a fish for food.")
	choice = input("Choose: ")
	check_action(choice, 3)
	if choice == "1":
		choice_5()
	elif choice == "2":
		if random.random() < 0.4:
			print("You go for a swim in the river and drown. Game over.")
		else:
			print("You catch a fish and gain strength.")
			choice_5()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_3()
		
def choice_4():
	print("\n1. Enter the cave.\n2. Keep walking past it.")
	choice = input("Choose: ")
	check_action(choice, 4)
	if choice == "1":
		if random.random() < 0.5:
			print("A bear is inside the cave. It attacks you. Game over.")
		else:
			print("You find supplies left by an explorer.")
			choice_6()
	elif choice == "2":
		choice_6()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_4()
		
def choice_5():
	print("\n1. Build a boat to escape.\n2. Keep walking along the river.")
	choice = input("Choose: ")
	check_action(choice, 5)
	if choice == "1":
		if random.random() < 0.6:
			print("Your boat breaks apart and you drown. Game over.")
		else:
			print("Your boat floats! You travel down the river.")
			choice_7()
	elif choice == "2":
		choice_7()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_5()
		
def choice_6():
	print("\n1. Climb a mountain for a better view.\n2. Search for signs of humans.")
	choice = input("Choose: ")
	check_action(choice, 6)
	if choice == "1":
		if random.random() < 0.7:
			print("You fall and die. Game over.")
		else:
			print("You see smoke in the distance.")
			choice_8()
	elif choice == "2":
		choice_8()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_6()
		
def choice_7():
	print("\n1. Try to signal for help.\n2. Keep moving forward.")
	choice = input("Choose: ")
	check_action(choice, 7)
	if choice == "1":
		if random.random() < 0.8:
			print("Nobody sees your signal. You die alone in the forest. Game over.")
			return
		else:
			print("A rescue team finds you! You are saved.")
			return
	elif choice == "2":
		choice_9()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_7()
		
def choice_8():
	print("\n1. Head toward the smoke.\n2. Avoid it and continue alone.")
	choice = input("Choose: ")
	check_action(choice, 8)
	if choice == "1":
		if random.random() < 0.85:
			print("It was a bandit camp. They kill you. Game over.")
		else:
			print("It was a friendly group of campers. You are saved!")
	elif choice == "2":
		choice_9()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_8()
		
def choice_9():
	print("\n1. Build a shelter and survive.\n2. Try to hike out of the forest.")
	choice = input("Choose: ")
	check_action(choice, 9)
	if choice == "1":
		if random.random() < 0.9:
			print("You can't find enough food and die. Game over.")
		else:
			print("You learn to survive and eventually get rescued!")
	elif choice == "2":
		choice_10()
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_9()
		
def choice_10():
	print("\n1. Follow the sun to navigate.\n2. Use the stars at night.")
	choice = input("Choose: ")
	check_action(choice, 10)
	if choice == "1":
		if random.random() < 0.95:
			print("You get lost and die of hunger. Game over.")
		else:
			print("You find a road and hitchhike to safety!")
	elif choice == "2":
		print("You reach a town after days of walking. You survived!")
	else:
		if choice.lower() != "save" and choice.lower() != "end":
			print("Invalid choice. Try again.")
		choice_10()
		
def Restart():
	# This function asks the player if they want to play again.
	while True:
		answer = input("Do you want to play again? (Yes/No)\n")
		if answer.lower() == "yes":
			return True
		elif answer.lower() == "no":
			return False
		else:
			print("Invalid input, try again")


while True:
	while True:
		choice_s = input("Welcome to the game!!\nDo new game or load save file? (new/load)\n")
		choice_s = choice_s.strip(" ")
		if choice_s.lower() == "load":  #checks for save file
				loaded = False
				try:
					file = open('save.txt','r')
					print("Game loaded\n")
					choice = file.read(1) #gets the number of the saved choice
					loaded = True
					file.close()
					# Redirects to the saved option
					if choice == "1":
						choice_1()
					elif choice == "2":
						choice_2()
					elif choice == "3":
						choice_3()
					elif choice == "4":
						choice_4()
					elif choice == "5": 
						choice_5()
					elif choice == "6":
						choice_6()
					elif choice == "7":
						choice_7()
					elif choice == "8":
						choice_8()
					elif choice == "9":
						choice_9()
					elif choice == "10":
						choice_10()
				except:
					if loaded:  # If the game did load the game
						sys.exit(0)
					print("No save file detected.")
		elif choice_s.lower() == "new":
			break
		else:
			print("Invalid input try again")
					
				
	start_game()
	again = Restart()
	if again == False:
		break
	

			
	
