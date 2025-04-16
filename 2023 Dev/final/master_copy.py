#! \users\Sohail Sayeed\AppData\local\Programs\python
# Legacy /usr/local/bin/python3

# This is the master copy for the game BlackSmith ported by Sohail Sayeed from the game 
# Talos Principle, all rights are reserved for the owner.

#######################################################################################################

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
        

