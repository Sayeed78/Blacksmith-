
# This file contains the prompts for the main menue of the game.
# This features three main storylines and a secret forth storyline
# if the player manages to complete each other storyline by collecting.
# the key items.

#######################################################################################################

# This func makes the initial storylines, asks for player for a number and returns a string of it
# This fucn is used by 'choice = player_choices()'
def player_choices():
        dialog(1, 'The Scholar')
        dialog(2, 'The Artist')
        dialog(3, 'The Scientist')
        dialog(4, 'Exit')
        print()
        choice = str(input('Choice? (only enter a single number): '))
        return choice

# Takes choice from above func, loops if its an acceptable answer, and returns the storyline function
def player_answers(choice):
        if choice == '1':
                return scholar()
        elif choice == '2':
                return artist()
        elif choice == '3':
                return scientist()
        elif choice == '4':
                exit()
        else:
                wrong_answer()
                print()
                return player_choices()
        
# Func Allows for a choice loop
def choice_loop():
        choice = player_choices() 
        if choice == '1':
                print('NORMAL')
                return player_answers(choice)
        
        elif choice == '2':
                print('NORMAL')
                return player_answers(choice)
        
        elif choice == '3':
                print('NORMAL')
                return player_answers(choice)
        
        elif choice == '4':
                print('NORMAL')
                return player_answers(choice)
        
        else:       
                wrong_answer()
                return choice_loop()

# Below code is for the secret player choices/answers

# This func makes the secret character choices
def player_choices_secret():
        dialog(1, 'The Scholar')
        dialog(2, 'The Artist')
        dialog(3, 'The Scientist')
        dialog(4, 'The Blacksmith')
        dialog(5, 'Exit')
        print()
        choice = str(input('Choice? (only enter single number): '))
        print()
        return(choice)

# Character answers with secret
def player_answers_secret(choice):
	count = 0
	if choice == '1':
		scholar()
	elif choice == '2':
		artist()
	elif choice == '3':
		scientist()
	elif choice == '4':
		blacksmith()
	elif choice == '5':
		exit()
	else:
		wrong_answer()
		print()
		return player_choices_secret()
	
# Func Allows for a choice loop but for secret path
def choice_loop_secret():
        if choice == ('1' or '2' or '3' or '4'):
                choice = player_choices_secret()
                print('SECRET')
                return player_answers_secret(choice)
        else:       
                wrong_answer()
                return choice_loop_secret()

	
########################################################################################################

# Below method is used to generate the secret menu and is used to see if the player
# has gathered required items to progress the individual storylines. For the main menu, if the
# the user has completed all other storylines, then the secret menu opens up unlocking the forth
# and final storyline. 

# This method might be able to reduced by using inventory.index(item).
# However, further research shows that .index() assumes the item is there,
# so if the item is not found a ValueError will occur. So the current
# code is sufficent. 

# Inventory check to show hidden blacksmith option and to check for items.
def item_check(item):
	check = 0
	for line in inventory:
		if line == str(item):
			check = 1
	return check

################################################################################################
