#! \users\Sohail Sayeed\AppData\local\Programs\python
# Legacy /usr/local/bin/python3

# This is the master copy for the game BlackSmith ported by Sohail Sayeed from the game Talos Principle, all rights reserved.

########################################################################################################
# Below functions deal with creating text boxs and reading text

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
        if number_spaces < 23:
                print('--------------------------')

        else:
                print('-------------------------------------------------------------------')

# This func deals with the whitespace the box and appropriates its length
def dialog_box_whitespace(number_spaces):
        if number_spaces < 23:
                while number_spaces  != 19:
                        print(' ', end = '')
                        number_spaces += 1
        else:
                while number_spaces != 60:
                        print(' ',end = '')
                        number_spaces += 1
        print('|')

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

# This function reads a txt doc line by line fast
def read_line_fast(file):
	with open(file) as fp:
		line = fp.readline()
		cnt = 1
		print(' --------------------------------------------------------------------------------')
		while line:
			print("| {}".format(line.strip()))
			line = fp.readline()
			if cnt <= 2:
				time.sleep(.5)
			elif  cnt == 3:
				 time.sleep(.5)
			elif cnt == 9:
				time.sleep(1.5)
			else:
				time.sleep(.5)
			cnt += 1
		print()
		print(' --------------------------------------------------------------------------------')


############################################################################################################


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

#######################################################################################################
# Break from into to player choices

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

# This Func might be able to reduced by using inventory.index(item).
# However, further research shows that .index() assumes the item is there,
# so if the item is not found a ValueError will occur. So the current
# code is sufficent. 

# Inventory check to show hidden blacksmith option
def item_check(item):
	check = 0
	for line in inventory:
		if line == str(item):
			check += 1
	return check

################################################################################################



#################################################################################################
# This section is for scholar storyline 

# Helper function to pause text as it is printed
def print_with_pause(text_list):
    for text, pause in text_list:
        print(text)
        time.sleep(pause)

# This is the intro Scholar text for the scholar path. 
# Potentially putting this in a sepereate text file that may be a better method of printing with pause
def scholar_text():
    scholar_intro_text = [
        ('XXXXXXXXXXXXXXXXXXXXXXXX', .1),
        ('XXTHE BLOOD OF SCHOLARSX', .1),
        ('XXXXXXXXXXXXXXXXXXXXXXXX', .1),
        ('XSHALL OUTWEIGTHXXXXXXXX', 2),
        ('XXXXXXXXXXXXXXXXXXXXXXXX', .1),
        ('XXTHE BLOOD OF MARTYRSXX', .1),
        ('XXXXXXXXXXXXXXXXXXXXXXXX', .1),
        ('', 0),
        ('You are Arkady', 0.5),
        ('        the Scholar', 0.5),
        ('        the Chronicler', 0.5),
        ('        the Sage', 0.5),
        ('', 0),
        ('XX The world has been consumed by ice. XXXX', 1),
        ('XX In the Last Monastery XXXXXXXXXXXXXXXXXX', 1),
        ('XX of the land of Faith, XXXXXXXXXXXXXXXXXX', 1),
        ('XX you complete the thoughts of the dead XX', 1),
        ('XXXXXXX that God might know who they were X,', 1),
        ('', 0),
        ('The hazy ghost of Weariness is always upon you, breaking your will. ', .1),
        ('You fear that you may fail before the Great Work is finished.', .1),
        ('', 0)
    ]
    print_with_pause(scholar_intro_text)

'''
Use case:
scholar_text()

Result:
Prints out the text with pauses at specific places.
'''

'''
# Below is the obsolete method of printing the scholar intro text. 
'
# This is the intro Scholar text for the scholar path. 
# Potentially putting this in a sepereate text file that may be a better method of printing with pause
def scholar_text():
        print('XXXXXXXXXXXXXXXXXXXXXXXX')
        print('XXTHE BLOOD OF SCHOLARSX')
        print('XXXXXXXXXXXXXXXXXXXXXXXX')
        time.sleep(2)
        print('XSHALL OUTWEIGTHXXXXXXXX')
        print('XXXXXXXXXXXXXXXXXXXXXXXX')
        print('XXTHE BLOOD OF MARTYRSXX')
        print('XXXXXXXXXXXXXXXXXXXXXXXX')
        print()
        time.sleep(2)
        print('You are Arkady')
        time.sleep(.5)
        print('        the Scholar')
        time.sleep(.5)
        print('        the Chronicler')
        time.sleep(.5)
        print('        the Sage')
        print('')
        time.sleep(1)
        print('XX The world has been consumed by ice. XXXX')
        time.sleep(1)
        print('XX In the Last Monastery XXXXXXXXXXXXXXXXXX')
        time.sleep(1)
        print('XX of the land of Faith, XXXXXXXXXXXXXXXXXX')
        time.sleep(1)
        print('XX you complete the thoughts of the dead XX')
        time.sleep(1)
        print('XXXXXXX that God might know who they were X,')
        time.sleep(1)
        print()
        print('The hazy ghost of Weariness is always upon you, breaking your will. ')
        print('You fear that you may fail before the Great Work is finished.')
        print()
'''
########################################################################################################
        



# Func goes through y/n work loop
def work():
        g2g = 0
        dialog(1, 'Work')
        answer = input('Choice?: ')
        while g2g != 1:
                if answer == '1':
                        g2g = 1
                        return answer
                elif answer == '1':
                        g2g = 1
                else:
                        g2g = 1
                        wrong_answer()
                        return work()

# Func goes through work/break dialog loop
def work_break():
        g2g = 0
        dialog(1, 'continue working')
        dialog(2, 'Take a break')
        answer = input('Choice? ')
        while g2g != 1:
                if answer == '1':
                        g2g = 1
                        return '1'
                elif answer == '2':
                        g2g = '1'
                        return 2
                else:
                        g2g = '1'
                        wrong_answer()
                        return work_break()



# This pulls up the scholar path of the game
# A list is created to determine choices 
def scholar():
        scholar_list = []
        work_choice_results = 0
        scholar_text()
#        read_line_fast("scholar.txt")
        work()
        print('You spend many days in the Library.')
        print('transcribing the work of the Ancient Poets.')
        print('         You learn much')
        print('         of thier dedication to the Sublime.')
        print()
        print('Your work is interrupted by a young monk:')
        print('"Come, brother! You deserve a break. Let us sing the old songs." ')
        print('')
        answer = work_break()
        if answer == '1':
                work_choice_results += 1
                print('You spend many days in the Library.')
                print('transcribing the work of the Ancient Philosophers.')
                print('         You learn much')
                print('         of thier confusion.')
                print()
                print('Your work is interrupted by a young monk:')
                print('"Come, brother! We have opened a barrel of wine!" ')
                print('')
        elif answer == '2':
                print('In the kitchens, the young brothers sing       ')
                print('XXXXX                      the old songs       ')
                print('XXXXX                      as if they were new.')
                print()
                print('Your spirit is renewed, but you lose precious time.')
                print()
                work()
        print('You spend many days in the Library.')
        print('transcribing the work of the Ancient Philosophers.')
        print('         You learn much')
        print('         of thier confusion.')
        print()
        print('Your work is interrupted by a young monk:')
        print('"Come, brother! We have discovered a strange miricle!"')
        print('')
        answer = work_break()
        if answer == '1':
                work_choice_results += 1
                print('You spend many days in the Library.')
                print('transcribing the work of the Ancient Philosophers.')
                print('         You learn much')
                print('         of thier confusion.')
                print()
                print('Your work is interrupted by a monk:')
                print('"Come, brother! We have discovered a strange miricle!"')
                print('')
        elif answer == '2':
                print('In the kitchens, the young brothers sing       ')
                print('XXXXX                      the old songs       ')
                print('XXXXX                      as if they were new.')
                print()
                print('Your spirit is renewed, but you lose precious time.')
                print()
                work()
        print(answer)
############################################################################################################

# The Artist story line
def artist():
        print(' The Artist')
        return 2

############################################################################################################

# The Scientist story line
def scientist():
        print('XXXXXXXXXXXXXXXXXXXXXXXXX')
        print('XX THE TRUE METHOND XXXXX')
        print('XXXXXXXXXXXXXXXXXXXXXXXXX')
        print('XXXX OF KNOWLEDGE XXXXXXX')
        print('XXXXXXXXXXXXXXXXXXXXXXXXX')
        print('XXXX EXPERIMENT XXXXXXXXX')
        print('XXXXXXXXXXXXXXXXXXXXXXXXX')
        print()
        print('You are Alexandra')
        print('        the Scientest')
        print('        whose curse & blessing is the Truth')
        print()
        print('There is no more life. Only the sands move in the Land of Death.')
        print()
        print('But there is hope:')
        print('       where this tomb')
        print('       is hidden the seed')
        print('       of the TREE OF LIFE')
        print()
        print('The hazy ghost of Weariness is always upon you, breaking your will.')
        print('You fear that tyou may fail before the Great Work is finished.')
        print()
        #dialog(1, 'Seek The Seed of Life')
        print()
        print('      XX')
        #time.sleep(.2)
        print('    XXXXXX')
        #time.sleep(.2)
        print('  XXXXXXXXXX')
        #time.sleep(.2)
        print('XXXXXXXXXXXXXX')
        #time.sleep(.2)
        print()
        print('NONE WHO DESCEND INTO THIS TOMB SHALL RETURN')
        print()
        dialog(1,'ENTER THE TOMB')
        print()
        print('XXXXXXX Stairs lead down')
        print('XXXXXXXXXXXXXXX to the dark chambers')
        print('XXXXXXXXXXXXXXXXXXXXXXX in the heart of the Earth')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX where the Seed awaits the Light')
        print()
        dialog(1, "Enter the Sage's Chamber")
        dialog(2,'Descend')
        ans = int(input('?: '))
        if ans == 1:
                print()
                print('The ghost of the Ancien Sage speaks.')
                print()
                print('I have beheld the wonders of the cosomos:')
                print('                          the fire of a million suns')
                print('                          the wind amoungst the starts')
                print('                          the black silence between the worlds')
                print('and now my heart is full o9f fear')
                print('for I know:')
                print('           the world was not made for us.')
                print()
                dialog(1, Descend)
                input('Decend?: ')
        return 3

############################################################################################################

# The Blacksmith
def blacksmith():
        print('The Blacksmith')
        return 4

############################################################################################################


####################################################################################################################        

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
        choice_loop_secret()
else:
        choice_loop()
        

