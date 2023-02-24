#! \users\Sohail Sayeed\AppData\local\Programs\python
# Legacy /usr/local/bin/python3

# This is the intro for the game BlackSmith

# This following three functions create the dialog box and the dialog box length

# This Function makes dialog box extend based on length of string
def dialog(num, message):
        message = str(message)
        number_spaces = len(list(message))
        dialog_box_length(number_spaces)
        print("|",num, ".", message, end = '')
        dialog_box_whitespace(number_spaces)
        dialog_box_length(number_spaces)

# This makes the top/bottom of the box
def dialog_box_length(number_spaces):
        if number_spaces < 28:
                print('-------------------------------')

        else:
                print('-------------------------------------------------------------------')

# This func deals with the whitespace the box and appropriates its length
def dialog_box_whitespace(number_spaces):
        if number_spaces < 28:
                while number_spaces  != 24:
                        print(' ', end = '')
                        number_spaces += 1
        else:
                while number_spaces != 60:
                        print(' ',end = '')
                        number_spaces += 1
        print('|')

# This func creates the unacceptable answer prompt
def wrong_answer():
	print()
	print("Sorry, that is not an accepteable answer.")

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

# This function reads a txt doc slowly line by line
def read_line(file):
	with open(file) as fp:
		line = fp.readline()
		cnt = 1
		print(' --------------------------------------------------------------------------------')
		while line:
			print("| {}".format(line.strip()))
			line = fp.readline()
			if cnt <= 2:
				time.sleep(1)
			elif  cnt == 3:
				 time.sleep(2)
			elif cnt == 8:
				time.sleep(3.5)
			else:
				time.sleep(1)
			cnt += 1
		print(' --------------------------------------------------------------------------------')

# This func makes the initial storylines, asks for player for a number and returns a string of it
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

# Inventory check to show hidden blacksmith option
def item_check(item):
	check = 0
	for line in inventory:
		if line == str(item):
			check += 1
	return check

##################################################

# Func goes through y/n work loop
def work():
        g2g = 0
        answer = input('Work? y or n: ')
        while g2g != 1:
                if answer == 'n':
                        g2g = 1
                        return work()
                elif answer == 'y':
                        g2g = 1
                else:
                        g2g = 1
                        wrong_answer()
                        return work()

# Func goes through work/break dialog loop
def work_break():
        g2g = 0
        dialog(1, 'Work')
        while g2g != 1:
                if answer == 'n':
                        g2g = 1
                        return work()
                elif answer == 'y':
                        g2g = 1
                else:
                        g2g = 1
                        wrong_answer()
                        return work()


# This Is the Scholar txt for the scholar path
def scholar_text():
        print()
        print('XXXXXXXXXXXXXXXXXXXXXXXX')
        print('XXTHE BLOOD OF SCHOLARSX')
        print('XXXXXXXXXXXXXXXXXXXXXXXX')
        print('XSHALL OUTWEIGTHXXXXXXXX')
        print('XXXXXXXXXXXXXXXXXXXXXXXX')
        print('XXTHE BLOOD OF MARTYRSXX')
        print('XXXXXXXXXXXXXXXXXXXXXXXX')
        print()
        print('You are Arkady')
        print('        the Scholar')
        print('        the Chronicler')
        print('        the Sage')
        print('')
        print('XX The world has been consumed by ice. XXXX')
        print('XX In the Last Monastery XXXXXXXXXXXXXXXXXX')
        print('XX of the land of Faith, XXXXXXXXXXXXXXXXXX')
        print('XX you complete the thoughts of the dead XX')
        print('XXXXXXX that God might know who they were X,')
        print()
        print('The hazy ghost of Weariness is always upon you, breaking your will. ')
        print('You fear that you may fail before the Great Work is finished.')
        print()

# This pulls up the scholar path of the game
def scholar():
        scholar_text()
        work()
        
        

################################################################################

# The Artist
def artist():
        print(' The Artist')
        return 2

# The Scientist story line
def scientist():
        print(' The Scientist')
        return 3

# The Blacksmith
def blacksmith():
        print('The Blacksmith')
        return 4

####################################################

import time
inventory = []
print()
print()
print()
print(' ------------------ ')
print('| Close your eyes. |')
print(' ------------------ ')
#time.sleep(3)
print()
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('     X               X      ')
print('    X X  JERUSALEM  X X     ')
print('     X               X      ')
print('A VISION OF THE ETERNAL CITY')
print('   XX XXXXXXXXXXXXXXX XXX   ')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print()
#begin()
#time.sleep(.5)
print('.')
#time.sleep(1.5)
print ('..')
#time.sleep(1.5)
print('...')
#time.sleep(1.5)
print('....')
#time.sleep(1.5)
print()
#read_line("intro.txt")
#time.sleep(5)
print()
#remember()
print()
print(' ---------- ')
print('| Remember |')
print(' ---------- ')
print()
#time.sleep(2)
#read_line("intro2.txt")
#time.sleep(6)
print()
#dream()
print()
print(' --------- ')
print('|  Dream  |')
print(' --------- ')
print()
#time.sleep(2)
print('....')
#time.sleep(.5)
print('...')
#time.sleep(.5)
print('..')
#time.sleep(.5)
print('.')
#time.sleep(1.5)
print()
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
#time.sleep(.75)
print('This is the dream of the giant ANTHROPOS     ')
#time.sleep(.75)
print('    whose body lies in the ruins of Jerusalem')
#time.sleep(.75)
print('    awaiting the day of awakening            ')
#time.sleep(.75)
print()
#time.sleep(.75)
print('                      This is your journey.  ')
print()
# Below code in yellow is for test purposes
#print(inventory)
#inventory.append('coin')
#print(inventory)
check = item_check('coin')
#print(check,'CHECK')
if check == 1:
        g2g = 0
        while g2g == 0: 
                choice = player_choices_secret()
                player_answers_secret(choice)
                print('SECRET')
                g2g = 1
else:
        g2g = 0
        while g2g == 0:
                choice = player_choices()
                player_answers(choice)
                print('NORMAL')
                g2g = 2
