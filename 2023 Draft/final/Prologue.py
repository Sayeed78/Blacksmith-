# This file contains the prologue dialog and functions

# This class contains the dialog methods that allow the player to 
# make choices. They use a simple binary way of answering.
class Prologue:
    def __init__(self, menu) -> None:
        self.menu = menu


    # This method prints the dialogue with a delay
    def print_dialogue(dialogue):
        for line, delay in dialogue:
            print(line)
            time.sleep(delay)

    # Below methods are for the initial start of the game.

    # The starting portion of intro and first choice loop
    def begin(self):
        while True:
            answer = input('Begin? y or n: ')
            if answer == 'n':
                print('\nYou awake from your dream.\n')
                exit()
            elif answer == 'y':
                print('\n --------------\n| Begin Vision |\n --------------')
                break
            else:
                menu.wrong_answer()

    # Func goes through remember/dialog loop
    def remember():
        while True:
            answer = input('Remember? y or n: ')
            if answer == 'n':
                continue
            elif answer == 'y':
                break
            else:
                menu.wrong_answer()

    # Func goes through dream/dialog loop
    def dream():
        while True:
            answer = input('Dream? y or n: ')
            if answer == 'n':
                continue
            elif answer == 'y':
                break
            else:
                menu.wrong_answer()

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


    # This method Starts the prologue
    def start_prologue(self):
        prologue_dialog_intro = [
            ('\n\n\n', 0),
            (' ------------------ ', 0)
            ('| Close your eyes. |', 0)
            (' ------------------ ', 3)
            ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX', .5)
            ('     X               X      ', .5)
            ('    X X  JERUSALEM  X X     ', .5)
            ('     X               X      ', .5)
            ('A VISION OF THE ETERNAL CITY', .5)
            ('   XX XXXXXXXXXXXXXXX XXX   ', .5)
            ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 5)
        ]

        prologue_dialog_begin = [
            ('.')
            ('..')
            ('...')
            ('....')
            (' ---------- ')
            ('| Remember |')
            (' ---------- ')
            (' --------- ')
            ('|  Dream  |')
            (' --------- ')
            ('....')
            ('...')
            ('..')
            ('.')
            ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            ('This is the dream of the giant ANTHROPOS     ')
            ('    whose body lies in the ruins of Jerusalem')
            ('    awaiting the day of awakening            ')
            ('                      This is your journey.  ')
        ]

        def __main__():
            self.print_dialogue(prologue_dialog_intro)
            self.begin()
            self.print_dialogue(prologue_dialog_begin)
            self.remember()
            self.read_line("prologue_dream.txt")
            self.dream()







'''
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
        self.begin()
        self.remember()
        self.dream()
            '''