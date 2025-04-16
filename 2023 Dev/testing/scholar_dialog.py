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
# CW = if only CW -> Priests else -> Kitches Are Empty
# TB = Kitches Are Empty

# Priests
# CW = Cold Claims You
# LW = Look For Wood

# Prologue 1 ################################################################################################

'XXXXXXXXXXXXXXXXXXXXXXXXXX'
'XX THE BLOOD OF SCHOLARS X'
'XXXXXXXXXXXXXXXXXXXXXXXXXX'

'X SHALL OUTWEIGTH XXXXXXXX'
'XXXXXXXXXXXXXXXXXXXXXXXXXX'
'XX THE BLOOD OF MARTYRS XX'
'XXXXXXXXXXXXXXXXXXXXXXXXXX'


'You are Arkady'
'        the Scholar'

'        the Chronicler'

'        the Sage'
''

'XX The world has been consumed by ice. XXXX'

'XX In the Last Monastery XXXXXXXXXXXXXXXXXX'

'XX of the land of Faith, XXXXXXXXXXXXXXXXXX'

'XX you complete the thoughts of the dead XX'

'XXXXXXX that God might know who they were X,'


'The hazy ghost of Weariness is always upon you, breaking your will. '
'You fear that you may fail before the Great Work is finished.'

,

# Note there is only one choice here
# W = Poets

# 1. Poets / First Dialog ###############################################################################################


'You spend many days in the Library.'

'transcribing the work of the Ancient Poets.'
'         You learn much'
'         of thier dedication to the Sublime.'


'Your work is interrupted by a young monk:'
'"Come, brother! You deserve a break. Let us sing the old songs." '
''
,

# CW = Philosophers
# TB = Young Brothers Sing Old Songs As New -> Playwrights

# Work Choices #######################################################################################################
############################################################################################################################

# 2. Philosophers ###############################################################################################


'You spend many days in the Library.'
'transcribing the work of the Ancient Philosophers.'
'         You learn much'
'         of thier confusion.'

'Your work is interrupted by a young monk:'
'"Come, brother! We have opened a barrel of wine!" '

,
# CW = Playwrights
# TB = Young Brothers Drink Live Forever

# 3. Playwrights ###############################################################################################


'You spend many days in the Library.'
'transcribing the work of the Ancient Playwrights.'
'         You learn much'
'         of of the human paradox.'

'Your work is interrupted by a monk:'
'"Come, brother! We have discovered a strange miricle!"'

,
# CW = Engineers
# TB = Brothers observe small animal blessed -> Mystics

# 4. Engineers ###############################################################################################


'You spend many days in the Library.'
'transcribing the work of the Ancient Engineers'
'         You learn much''         of how the world was made.'

'Your work is interrupted by a monk:'
'"Come, brother! Let us sing the old songs once more!"'

,
# CW = Mystics
# TB = Brothers Sing Old Songs Not Forgotten -> Geographers

# 5. Mystics ###############################################################################################


'You spend many days in the Library.'
'transcribing the work of the Ancient Mystics'
'         You learn much'
'         of what the ancients feared.'

'Your work is interrupted by an old monk:'
'"Come, brother! We have opened the last barrel of wine!"'

,
# CW = Geographers
# TB = Old Brothers Drink End is Nigh -> Priests 

# 6. Geographers ###############################################################################################

'You spend many days in the Library.'
'transcribing the work of the Ancient Geographers.'
'         You learn much'
'         of how the world changed.'

'Your work is not interrupted.'

,
# CW = Priests 
# TB = Kitches Are Empty


# Break Choices #######################################################################################################
###############################################################################################################################

# 1. Young Brothers sing old songs ###############################################################################################

,
'In the kitchens, the young brothers sing'
'XXXXX                      the old songs'
'XXXXX                      as if they were new.'

'Your spirit is renewed, but you lose precious time.'

,
# CW = Playwrights

# 2. Young Brothers Drink and Laugh ###############################################################################################

'In the kitchens, the young brothers drink'
'XXXXX                           and laugh'
'XXXXX                           as if they will live forever.'

'Your spirit is renewed, but you lose precious time.'

,
# CW = Engineers

# 3. Brothers observe small animal blessed happiness ###############################################################################################

'In the kitchens, the brothers observe       '
'XXXXX                      a small animal       '
'XXXXX                      that is blessed to bring happiness.'

'Your spirit is renewed, but you lose precious time.'

,
# CW = Mystics

# 4. Old Songs Not Forgotten ###############################################################################################

'In the kitchens, the brothers sing'
'XXXXX                the old songs'
'XXXXX                that they have not forgotten.'

'Your spirit is renewed, but you lose precious time.'

,
# Engineers -> here
# CW = Geographers

# 5. Old Brothers Drink End is Nigh ###############################################################################################

'In the kitchens, the old brothers drink'
'XXXXX                         and laugh'
'XXXXX                          knowing the end is nigh.'

'Your spirit is renewed, but you lose precious time.'

,
# CW = Priests

# 6. Kitches Empty ###############################################################################################

'The kitchens are empty.'
'XXXXX                  '
'XXXXX                  '

'You lose precious time.'

,
# Geographers -> here
# CW = Priests

################################################################################################
# Ending Dialogue Sequence ###############################################################################################

# Geographers ###############################################################################################

'You spend many days in the Library.'
'transcribing the work of the Ancient Geographers.'
'         You learn much'
'         of how the world changed.'

'Your work is not interrupted.'

,
# Preiests / Ending Sequence ###############################################################################################

'You spend many days in the Library.'
'transcribing the work of the Ancient Priests.'
'         You learn much'
'         of how the Word of God was lost.'

'Your have run out of wood for the furnance.'
'                           It is very cold.'

,
# CW = Cold Claims You
# LW = Look For Wood


# Look For Wood ###############################################################################################


'XX there is no more wood XX'
'XX nor an axe with which XX'
'XX to cut more           XX'

,
# CW = Cold Claims You

# Cold Claims You ###############################################################################################


'You spend many days in the Library.'
'until the cold claims you.'
'         You learn much'
'         of regret.'

'The Great Work remains unfinished.'


# CW = restart
# TB = restart 

################################################################################################
