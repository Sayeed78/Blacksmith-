# Scholar_Dialog for Draft


# List of dialog tree ###############################################################################################
# Looks like each dialog is in an array and when TB is taken, the next index is skipped ie. i += 1


# Poets
# CW = Philosophers
# TB = Young Brothers Sing Old Songs As New -> Playwrights

# Philosophers
# CW = Playwrights
# TB = Young Brothers Drink Live Forever ->Engineers

# Playwrights
# CW = Engineers
# TB = Brothers observe small animal blessed -> Mystics

# Engineers
# CW = Mystics
# TB = Brothers Sing Old Songs Not Forgotten -> Geographers

# Mystics
# CW = Geographers
# TB = Old Brothers Drink End is Nigh -> Priests

# Geographers
# CW = Priests 
# TB = Kitches Are Empty

# Priests
# CW = Cold Claims You
# LW = Look For Wood

# Prologue 1 ################################################################################################
def intro_text():
		print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
		print('XX THE BLOOD OF SCHOLARS X')
		print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
		#time.sleep(2)
		print('X SHALL OUTWEIGTH XXXXXXXX')
		print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
		print('XX THE BLOOD OF MARTYRS XX')
		print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
		print()
		#time.sleep(2)
		print('You are Arkady')
		print('        the Scholar')
		#time.sleep(.5)
		print('        the Chronicler')
		#time.sleep(.5)
		print('        the Sage')
		print('')
		#time.sleep(1)
		print('XX The world has been consumed by ice. XXXX')
		#time.sleep(1)
		print('XX In the Last Monastery XXXXXXXXXXXXXXXXXX')
		#time.sleep(1)
		print('XX of the land of Faith, XXXXXXXXXXXXXXXXXX')
		#time.sleep(1)
		print('XX you complete the thoughts of the dead XX')
		#time.sleep(1)
		print('XXXXXXX that God might know who they were X,')
		#time.sleep(1)
		print()
		print('The hazy ghost of Weariness is always upon you, breaking your will. ')
		print('You fear that you may fail before the Great Work is finished.')
		print()

# Note there is only one choice here
# W = Poets

# 1. Poets / First Dialog ###############################################################################################

def poet_text():
		print()
		print('You spend many days in the Library.')
		#time.sleep(.5)
		print('transcribing the work of the Ancient Poets.')
		print('         You learn much')
		print('         of thier dedication to the Sublime.')
		#time.sleep(.5)
		print()
		print('Your work is interrupted by a young monk:')
		print('"Come, brother! You deserve a break. Let us sing the old songs." ')
		print('')

# CW = Philosophers
# TB = Young Brothers Sing Old Songs As New -> Playwrights

# Work Choices #######################################################################################################
############################################################################################################################

# 2. Philosophers ###############################################################################################

def philosopher_text():
		print()
		print('You spend many days in the Library.')
		print('transcribing the work of the Ancient Philosophers.')
		print('         You learn much')
		print('         of thier confusion.')
		print()
		print('Your work is interrupted by a young monk:')
		print('"Come, brother! We have opened a barrel of wine!" ')
		print()

# CW = Playwrights
# TB = Young Brothers Drink Live Forever

# 3. Playwrights ###############################################################################################

def playwrights_text():
		print()
		print('You spend many days in the Library.')
		print('transcribing the work of the Ancient Playwrights.')
		print('         You learn much')
		print('         of of the human paradox.')
		print()
		print('Your work is interrupted by a monk:')
		print('"Come, brother! We have discovered a strange miricle!"')
		print()

# CW = Engineers
# TB = Brothers observe small animal blessed -> Mystics

# 4. Engineers ###############################################################################################

def engineers_text():
		print()
		print('You spend many days in the Library.')
		print('transcribing the work of the Ancient Engineers')
		print('         You learn much')print('         of how the world was made.')
		print()
		print('Your work is interrupted by a monk:')
		print('"Come, brother! Let us sing the old songs once more!"')
		print()

# CW = Mystics
# TB = Brothers Sing Old Songs Not Forgotten -> Geographers

# 5. Mystics ###############################################################################################

def mystics_text():
		print()
		print('You spend many days in the Library.')
		print('transcribing the work of the Ancient Mystics')
		print('         You learn much')
		print('         of what the ancients feared.')
		print()
		print('Your work is interrupted by an old monk:')
		print('"Come, brother! We have opened the last barrel of wine!"')
		print()

# CW = Geographers
# TB = Old Brothers Drink End is Nigh -> Priests 

# 6. Geographers ###############################################################################################

def geographers_text():
		print('You spend many days in the Library.')
		print('transcribing the work of the Ancient Geographers.')
		print('         You learn much')
		print('         of how the world changed.')
		print()
		print('Your work is not interrupted.')
		print()

# CW = Priests 
# TB = Kitches Are Empty


# Break Choices #######################################################################################################
###############################################################################################################################

# 1. Young Brothers sing old songs ###############################################################################################

def young_old_songs_text():
		print()
		print('In the kitchens, the young brothers sing')
		print('XXXXX                      the old songs')
		print('XXXXX                      as if they were new.')
		print()
		print('Your spirit is renewed, but you lose precious time.')
		print()

# CW = Playwrights

# 2. Young Brothers Drink and Laugh ###############################################################################################

def young_drink_laugh_text():
		print('In the kitchens, the young brothers drink')
		print('XXXXX                           and laugh')
		print('XXXXX                           as if they will live forever.')
		print()
		print('Your spirit is renewed, but you lose precious time.')
		print()

# CW = Engineers

# 3. Brothers observe small animal blessed happiness ###############################################################################################

def animal_blessed_text():
		print('In the kitchens, the brothers observe       ')
		print('XXXXX                      a small animal       ')
		print('XXXXX                      that is blessed to bring happiness.')
		print()
		print('Your spirit is renewed, but you lose precious time.')
		print()

# CW = Mystics

# 4. Old Songs Not Forgotten ###############################################################################################

def songs_not_forgotten_text():
		print('In the kitchens, the brothers sing')
		print('XXXXX                the old songs')
		print('XXXXX                that they have not forgotten.')
		print()
		print('Your spirit is renewed, but you lose precious time.')
		print()
		work()

# Engineers -> here
# CW = Geographers

# 5. Old Brothers Drink End is Nigh ###############################################################################################

def end_is_nigh_text():
		print('In the kitchens, the old brothers drink')
		print('XXXXX                         and laugh')
		print('XXXXX                          knowing the end is nigh.')
		print()
		print('Your spirit is renewed, but you lose precious time.')
		print()

# CW = Priests

# 6. Kitchens Empty ###############################################################################################

def kitchens_empty_text():
		print('The kitchens are empty.')
		print('XXXXX                  ')
		print('XXXXX                  ')
		print()
		print('You lose precious time.')
		print()

# Geographers -> here
# CW = Priests

################################################################################################
# Ending Dialogue Sequence ###############################################################################################

# 7. Priests / Ending Sequence ###############################################################################################

def priests_text():
		print('You spend many days in the Library.')
		print('transcribing the work of the Ancient Priests.')
		print('         You learn much')
		print('         of how the Word of God was lost.')
		print()
		print('Your have run out of wood for the furnance.')
		print('                           It is very cold.')
		print()

# CW = Cold Claims You
# LW = Look For Wood


# 8. Look For Wood ###############################################################################################

def look_for_wood_text():
		print()
		print('XX there is no more wood XX')
		print('XX nor an axe with which XX')
		print('XX to cut more           XX')
		print()

# CW = Cold Claims You

# Cold Claims You ###############################################################################################

def cold_claims_text():
		print()
		print('You spend many days in the Library.')
		print('until the cold claims you.')
		print('         You learn much')
		print('         of regret.')
		print()
		print('The Great Work remains unfinished.')
		print()

# CW = restart
# TB = restart 


################################################################################################
################################################################################################


# Draft func for list

work_break_results = 0 

def work_text():
	if work_break_results == 0:
		work_break_results += 2
		poet_text()

	elif work_break_results == 2:
		work_break_results += 2
		philosopher_text()	

	elif work_break_results == 4:
		work_break_results += 2
		playwrights_text()

	elif work_break_results == 6:
		work_break_results += 2
		engineers_text()

	elif work_break_results == 8:
		work_break_results += 2
		mystics_text()

	elif work_break_results == 10:
		work_break_results += 2
		geographers_text()


	else:
		return


def break_text():
	if work_break_results == 1:
		work_break_results += 3
		young_old_songs_text():

	elif work_break_results == 3:
		work_break_results += 3
		young_drink_laugh_text():

	elif work_break_results == 5:
		work_break_results += 3
		animal_blessed_text():

	elif work_break_results == 7:
		work_break_results += 3
		songs_not_forgotten_text():

	elif work_break_results == 9:
		work_break_results += 3
		end_is_nigh_text():

	elif work_break_results == 10:
		work_break_results += 2
		kitchens_empty_text():

	else:
		return
