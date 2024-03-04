
#################################################################################################
# This section is for Scholar storyline 
#################################################################################################

class ScholarPath:
        def __init__(self, main) -> None:
                self.main = main
                self.db = main.DialogBox(main)
                self.dp = main.DialogPrompts(self)


        # Helper function to pause text as it is printed. This is used with scholar_text() to slowly
        # print out the intro text
        def print_with_pause(self, text_list):
                for text, pause in text_list:
                        print(text)
                        time.sleep(pause)


        # This is the intro Scholar text. 
        # Putting this in a sepereate text file may potentially be a better method of printing with pause.
        # This current method does not allow for easy change in the script.
        # However, this current method works fine for what is needed.
        '''
        Use case:
        scholar_text()

        Result:
        Prints out the text with pauses at specific places.
        '''
        def scholar_text():
                normal_pause = 1
                quick_pause = .1
                short_pause = .5
                long_pause = 2
        
                scholar_intro_text = [
                ('XXXXXXXXXXXXXXXXXXXXXXXX', short_pause),
                ('XXTHE BLOOD OF SCHOLARSX', short_pause),
                ('XXXXXXXXXXXXXXXXXXXXXXXX', short_pause),
                ('XSHALL OUTWEIGTHXXXXXXXX', long_pause),
                ('XXXXXXXXXXXXXXXXXXXXXXXX', short_pause),
                ('XXTHE BLOOD OF MARTYRSXX', short_pause),
                ('XXXXXXXXXXXXXXXXXXXXXXXX', short_pause),
                ('', 0),
                ('You are Arkady', quick_pause),
                ('        the Scholar', quick_pause),
                ('        the Chronicler', quick_pause),
                ('        the Sage', quick_pause),
                ('', 0),
                ('XX The world has been consumed by ice. XXXX', normal_pause),
                ('XX In the Last Monastery XXXXXXXXXXXXXXXXXX', normal_pause),
                ('XX of the land of Faith, XXXXXXXXXXXXXXXXXX', normal_pause),
                ('XX you complete the thoughts of the dead XX', normal_pause),
                ('XXXXXXX that God might know who they were X,', normal_pause),
                ('', 0),
                ('The hazy ghost of Weariness is always upon you, breaking your will. ', short_pause),
                ('You fear that you may fail before the Great Work is finished.', short_pause),
                ('', 0)
        ]
                scholar_path.print_with_pause(scholar_intro_text)

#######################################################################################################

# These method deal with the player choices in the dialog tree. 

# Func goes through y/n work loop
        def work(self):
                self.db.dialog(1, 'Begin work.')
                answer = input('Choice?: ')
                if answer == '1':
                        return answer
                else:
                        self.dp.wrong_answer()
                        return self.work()

        # Func goes through work/break dialog loop
        def work_break(self):
                self.db.dialog(1, 'Continue working.')
                self.db.dialog(2, 'Take a break.')
                answer = input('Choice? ')
                if answer == '1':
                        return '1'
                elif answer == '2':
                        return 2
                else:
                        dp.wrong_answer()
                        return self.work_break()
                