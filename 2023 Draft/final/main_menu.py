
# This file contains the prompts for the main menue of the game.
# This features three main storylines and a secret forth storyline
# if the player manages to complete each other storyline by collecting.
# the key items.

#######################################################################################################

class main:
        def __init__(self) -> None:
                self.dp = dialog_prompts()
                self.scholar = scholar_path()
                self.artist = artist_path()
                self.scientist = scientist_path()
                self.blacksmith = blacksmith_path()


#######################################################################################################

# This func makes the initial storylines, asks for player for a number and returns a string of it
# This func is used by 'choice = player_choices()'
class DialogBox:
        def __init__(self, items) -> None:
                self.items = items

        # Below functions deal with creating text boxes and reading text
               
        def determine_box_length(self, message_length):
                return min(50, message_length + 7)  # Maximum box length is 50. Added 7 for "| num. " and some padding at the tail.
        
        def print_box_top_bottom(self, length):
                print('-' * length)
        
        def print_box_whitespace(self, message_length, box_length):
                spaces_to_add = box_length - message_length - 6  # Account for "| num. " in the box
                print(' ' * spaces_to_add + '|')

        # This following three functions create the dialog box and the dialog box length
        # This Function makes dialog box extend based on length of string
        def dialog(self, num, message):
                message = str(message)
                box_length = self.determine_box_length(len(message))
                self.print_box_top_bottom(box_length)
                print(f"| {num}. {message}", end='')
                self.print_box_whitespace(len(message), box_length)
                self.print_box_top_bottom(box_length)


########################################################################################################

# These two methods read in text files and either print fast or print slowly. These may be/become 
# obsolete.

class Read:
        def __init__(self) -> None:
                pass

        # This function reads a txt doc slowly line by line
        def read_line(self, file):
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
        def read_line_fast(self, file):
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

class DialogPrompts:
        def __init__(self, item, main) -> None:
                self.item = item
                self.db = DialogBox()
                

        # This func creates the unacceptable answer prompt
        def wrong_answer(self):
                print()
                print("Sorry, that is not an accepteable answer.")

        def player_choices(self):
                db = self.db
                db.dialog(1, 'The Scholar')
                db.dialog(2, 'The Artist')
                db.dialog(3, 'The Scientist')
                db.dialog(4, 'Exit')
                print()
                choice = str(input('Choice? (only enter a single number): '))
                return choice

        # Takes choice from above func, loops if its an acceptable answer, and returns the storyline function
        def player_answers(self, choice):
                if choice == '1':
                        return scholar_path()
                elif choice == '2':
                        return artist_path()
                elif choice == '3':
                        return scientist_path()
                elif choice == '4':
                        exit()
                else:
                        wrong_answer()
                        print()
                        return player_choices()
                
        # Func Allows for a choice loop
        def choice_loop(self):
                while True:
                        choice = player_choices()

                        if choice in {'1', '2', '3', '4'}:
                                player_answers(choice)
                                break
                        else:
                                wrong_answer()

        # Below code is for the secret player choices/answers
        # This func makes the secret character choices
        def player_choices_secret(self):
                db = self.db
                db.dialog(1, 'The Scholar')
                db.dialog(2, 'The Artist')
                db.dialog(3, 'The Scientist')
                db.dialog(4, 'The Blacksmith')
                db.dialog(5, 'Exit')
                print()
                choice = str(input('Choice? (only enter single number): '))
                print()
                return(choice)

        # Character answers with secret
        def player_answers_secret(self, choice):
                if choice == '1':
                        scholar_path()
                elif choice == '2':
                        artist_path()
                elif choice == '3':
                        scientist_path()
                elif choice == '4':
                        blacksmith_path()
                elif choice == '5':
                        exit()
                else:
                        wrong_answer()
                        print()
                        return player_choices_secret()
                
        # Func Allows for a choice loop but for secret path
        def choice_loop_secret(self):
                while True:
                        choice = player_choices_secret()

                        if choice in {'1', '2', '3', '4', '5'}:
                                player_answers_secret(choice)
                                break
                        else:
                                wrong_answer()


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
        def item_check(self, item):
                check = 0
                for line in inventory:
                        if line == str(item):
                                check = 1
                return check

################################################################################################

db = DialogBox([])
db.dialog(1, "The Scholar")
db.dialog(2, "The Artist______")
db.dialog(3, "The Scientist____________________________")       