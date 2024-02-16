#! /usr/local/bin/python3

# This is the Scholar path of the game Blacksmith

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
                print(' ------------------------------')

        else:
                print(' -----------------------------------------------------------------')

# This func deals with the whitespace the box and appropriates its length
def dialog_box_whitespace(number_spaces):
        if number_spaces < 28:
                while number_spaces  != 25:
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

# Dialog start 
def scholar_dialog_start
	answer = dialog(1,'Work')
	if answer = '1'
		
####################################################################
print( ' The Scholar')
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

