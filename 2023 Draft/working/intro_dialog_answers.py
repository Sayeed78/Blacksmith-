
# This file contains the dialog methods that allow the player to 
# make choices. They use a simple binary way of answering.

#######################################################################################################

# Below methods are for the inital start of the game.

# The starting portion of intro and first choice loop
def begin():
	g2g = 0
	answer = input('Begin? y or n: ')
	while g2g != 1:
		if answer == 'n':
			print()
			print('You awake from your dream.')
			print()
			exit()
		elif answer == 'y':
			g2g=1
			print()
			print(' --------------')
			print('| Begin Vision |')
			print(' --------------')
		else:
			wrong_answer()
			g2g = 1
			return begin()

# Func goes through remember/dialog loop
def remember():
	g2g = 0
	answer = input('Remember? y or n: ')
	while g2g != 1:
		if answer == 'n':
			g2g = 1
			return remember()
		elif answer == 'y':
			g2g = 1
		else:
			g2g = 1
			wrong_answer()
			return remember()

# Func goes through dream/dialog loop
def dream():
        g2g = 0
        answer = input('Dream? y or n: ')
        while g2g != 1:
                if answer == 'n':
                        g2g = 1
                        return dream()
                elif answer == 'y':
                        g2g = 1
                else:
                        g2g = 1
                        wrong_answer()
                        return dream()

#######################################################################################################
