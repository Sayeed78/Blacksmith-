
# This section is for Scholar storyline 

#################################################################################################

# Helper function to pause text as it is printed. This is used with scholar_text() to slowly
# print out the intro text

def print_with_pause(text_list):
    for text, pause in text_list:
        print(text)
        time.sleep(pause)


# This is the intro Scholar text. 
# Putting this in a sepereate text file may potentially be a better method of printing with pause.
# This current method does not allow for easy change in the script.
# However, this current method works fine for what is needed.
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

#######################################################################################################

# These method deal with the player choices in the dialog tree. 

# Func goes through y/n work loop
def work():
        g2g = 0
        dialog(1, 'Begin work.')
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
        dialog(1, 'Continue working.')
        dialog(2, 'Take a break.')
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