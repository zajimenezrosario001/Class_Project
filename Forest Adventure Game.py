#!/usr/bin/env python3

import random
import sys

def start_game():
	print("You wake up in a dark forest with no memory of how you got here. Your goal is to survive and find a way out.\nWrite 'save' to save the game or 'end' if you want to quit.")
	choice_1()

def save_game(current_choice):
	save = open("save.txt","w")
	save.write(str(current_choice))
	save.close()

def check_action(choice, level):
	if choice.lower() == "save":
		save_game(level)
	if choice.lower() == "end":
		sys.exit(0)
			
			
def choice_1():
	print("\n1. Follow a faint trail.\n2. Climb a tree to get a better view.")
	choice = input("Choose: ")
	check_action(choice, 1)
	if choice.lower() == "save":
			save_game("1")
			print("\nGame saved\n")
			choice_1()

	if choice == "1":
		choice_2()
	elif choice == "2":
		if random.random() < 0.2:
			print("You slip and fall to your death. Game over.")
		else:
			print("You see a river in the distance and decide to head that way.")
			choice_3()
	else:
		print("Invalid choice. Try again.")
		choice_1()
		
def choice_2():
	print("\n1. Keep following the trail.\n2. Go off the path into the trees.")
	choice = input("Choose: ")
	if choice == "1":
		choice_3()
	elif choice == "2":
		if random.random() < 0.3:
			print("You walk into a trap and die. Game over.")
		else:
			print("You find a cave entrance.")
			choice_4()
	else:
		print("Invalid choice. Try again.")
		choice_2()
		
def choice_3():
	print("\n1. Follow the river downstream.\n2. Try to catch a fish for food.")
	choice = input("Choose: ")
	if choice == "1":
		choice_5()
	elif choice == "2":
		if random.random() < 0.4:
			print("You go for a swim in the river and drown. Game over.")
		else:
			print("You catch a fish and gain strength.")
			choice_5()
	else:
		print("Invalid choice. Try again.")
		choice_3()
		
def choice_4():
	print("\n1. Enter the cave.\n2. Keep walking past it.")
	choice = input("Choose: ")
	if choice == "1":
		if random.random() < 0.5:
			print("A bear is inside the cave. It attacks you. Game over.")
		else:
			print("You find supplies left by an explorer.")
			choice_6()
	elif choice == "2":
		choice_6()
	else:
		print("Invalid choice. Try again.")
		choice_4()
		
def choice_5():
	print("\n1. Build a boat to escape.\n2. Keep walking along the river.")
	choice = input("Choose: ")
	if choice == "1":
		if random.random() < 0.6:
			print("Your boat breaks apart and you drown. Game over.")
		else:
			print("Your boat floats! You travel down the river.")
			choice_7()
	elif choice == "2":
		choice_7()
	else:
		print("Invalid choice. Try again.")
		choice_5()
		
def choice_6():
	print("\n1. Climb a mountain for a better view.\n2. Search for signs of humans.")
	choice = input("Choose: ")
	if choice == "1":
		if random.random() < 0.7:
			print("You fall and die. Game over.")
		else:
			print("You see smoke in the distance.")
			choice_8()
	elif choice == "2":
		choice_8()
	else:
		print("Invalid choice. Try again.")
		choice_6()
		
def choice_7():
	print("\n1. Try to signal for help.\n2. Keep moving forward.")
	choice = input("Choose: ")
	if choice == "1":
		if random.random() < 0.8:
			print("Nobody sees your signal. You die alone in the forest. Game over.")
		else:
			print("A rescue team finds you! You are saved.")
	elif choice == "2":
		choice_9()
	else:
		print("Invalid choice. Try again.")
		choice_7()
		
def choice_8():
	print("\n1. Head toward the smoke.\n2. Avoid it and continue alone.")
	choice = input("Choose: ")
	if choice == "1":
		if random.random() < 0.85:
			print("It was a bandit camp. They kill you. Game over.")
		else:
			print("It was a friendly group of campers. You are saved!")
	elif choice == "2":
		choice_9()
	else:
		print("Invalid choice. Try again.")
		choice_8()
		
def choice_9():
	print("\n1. Build a shelter and survive.\n2. Try to hike out of the forest.")
	choice = input("Choose: ")
	if choice == "1":
		if random.random() < 0.9:
			print("You can't find enough food and die. Game over.")
		else:
			print("You learn to survive and eventually get rescued!")
	elif choice == "2":
		choice_10()
	else:
		print("Invalid choice. Try again.")
		choice_9()
		
def choice_10():
	print("\n1. Follow the sun to navigate.\n2. Use the stars at night.")
	choice = input("Choose: ")
	if choice == "1":
		if random.random() < 0.95:
			print("You get lost and die of hunger. Game over.")
		else:
			print("You find a road and hitchhike to safety!")
	elif choice == "2":
		print("You reach a town after days of walking. You survived!")
	else:
		print("Invalid choice. Try again.")
		choice_10()
		
def Restart():
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
		choice_s = input("Welcome to the game!!\nDo new game or load save file? (new/load)")
		if choice_s.lower() == "load":
				try:
					file = open('save.txt','r')
					print("Game loaded\n")
					choice = file.read(1)
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
					print("No save file detected.")
		elif choice_s.lower() == "new":
			break
		else:
			print("Invalid input try again")
					
				
	start_game()
	again = Restart()
	if again == False:
		break
	

			
	
