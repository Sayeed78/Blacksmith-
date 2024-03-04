# first attempted at making a dialog class for game blacksmith
def __init__(self, num, message):
        self.num = num
        self.message = message

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
