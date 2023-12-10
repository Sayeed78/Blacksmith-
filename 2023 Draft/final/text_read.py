########################################################################################################

#Notes: It is possible to turn some of these frequent funcions into modules so they become easily importable to any file.

# Below functions deal with creating text boxs and reading text

# This following three functions create the dialog box and the dialog box length
# This Function makes dialog box extend based on length of string
def dialog(num, message):
    message = str(message)
    box_length = determine_box_length(len(message))
    print_box_top_bottom(box_length)
    print(f"| {num}. {message}", end='')
    print_box_whitespace(len(message), box_length)
    print_box_top_bottom(box_length)

def determine_box_length(message_length):
    return max(20, message_length + 4)  # Minimum box length is 23, adding 6 for "| num. " and some padding

def print_box_top_bottom(length):
    print('-' * length)

def print_box_whitespace(message_length, box_length):
    spaces_to_add = box_length - message_length - 6  # Account for "| num. " in the box
    print(' ' * spaces_to_add + '|')

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
