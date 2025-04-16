#! /usr/local/bin/python3

# This is the intro for the game BlackSmith

# This func creates the unacceptable answer prompt
def wrong_answer():
	print()
	print("Sorry, that is not an acceptable answer.")

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
			return start_answer()

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

# This function reads a txt doc slowly line by line
def read_line(file):
	with open(file) as fp:
		line = fp.readline()
		cnt = 1
		print(' -------------------------------------------------------------------------------')
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


####################################################

import time
print()
print()
print()
print(' ------------------ ')
print('| Close your eyes. |')
print(' ------------------ ')
time.sleep(3)
print()
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('     X               X      ')
print('    X X  JERUSALEM  X X     ')
print('     X               X      ')
print('A VISION OF THE ETERNAL CITY')
print('   XX XXXXXXXXXXXXXXX XXX   ')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print()
begin()
time.sleep(.5)
print('.')
time.sleep(1.5)
print ('..')
time.sleep(1.5)
print('...')
time.sleep(1.5)
print()
read_line("intro.txt")
time.sleep(5)
print()
remember()
print()
print(' ---------- ')
print('| Remember |')
print(' ---------- ')
print()
time.sleep(2)
#intro2 = open("intro2.txt", "r").read()
read_line("intro2.txt")
#print(intro2)
time.sleep(6)
print()
print(' --------- ')
print('|  Dream  |')
print(' --------- ')
print()
time.sleep(2)
print('...')
time.sleep(.5)
print('..')
time.sleep(.5)
print('.')
time.sleep(1.5)
print()
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
time.sleep(.25)
print('This is the dream of the giant ANTHROPOS     ')
time.sleep(.25)
print('    whose body lies in the ruins of Jerusalem')
time.sleep(.25)
print('    awaiting the day of awakening            ')
time.sleep(.25)
print()
time.sleep(.25)
print('                      This is your journey.  ')
time.sleep(.25)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


