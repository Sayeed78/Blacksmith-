# Scholar_Dialog for Draft

class Scholar_Dialog:
    def __init__(self) -> None:
        pass

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

    prologue_dialog = {
        
        'prologue':[
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
        ]
    }
# Note there is only one choice here
# W = Poets

work_dialog = {

# Poets / First Dialog ###############################################################################################

    'poets': [
        'You spend many days in the Library.'

        'transcribing the work of the Ancient Poets.'
        '         You learn much'
        '         of their dedication to the Sublime.'
        '                                           '
        '                                           '
        'Your work is interrupted by a young monk:'
        '"Come, brother! You deserve a break. Let us sing the old songs." '
        ''
    ],  

# CW = 'philosophers'
# TB = 'old_songs'

# Work Choices #######################################################################################################
############################################################################################################################

# 1. Philosophers ###############################################################################################


    'philosophers':[
        'You spend many days in the Library.'
        'transcribing the work of the Ancient Philosophers.'
        '         You learn much'
        '         of their confusion.'
        '                                                   '
        'Your work is interrupted by a young monk:'
        '"Come, brother! We have opened a barrel of wine!" '
    ],

# CW = 'playwrights'
# TB = 'dring_laugh'

# 2. Playwrights ###############################################################################################

    'playwrights':[
        'You spend many days in the Library.'
        'transcribing the work of the Ancient Playwrights.'
        '         You learn much'
        '         of the human paradox.'
        '                                                   '
        'Your work is interrupted by a monk:'
        '"Come, brother! We have discovered a strange miricle!"'
    ],

# CW = 'engineers'
# TB = 'small_animal'

# 3. Engineers ###############################################################################################

    'engineers':[
        'You spend many days in the Library.'
        'transcribing the work of the Ancient Engineers'
        '         You learn much''         of how the world was made.'
        '                                                           '
        'Your work is interrupted by a monk:'
        '"Come, brother! Let us sing the old songs once more!"'
    ],
# CW = 'mystics'
# TB = 'old_songs'

# 4. Mystics ###############################################################################################

    'mystics':[
        'You spend many days in the Library.'
        'transcribing the work of the Ancient Mystics'
        '         You learn much'
        '         of what the ancients feared.'
        '                                        '
        'Your work is interrupted by an old monk:'
        '"Come, brother! We have opened the last barrel of wine!"'
    ],
# CW = 'geographers'
# TB = 'end_is_nigh'

# 6. Geographers ###############################################################################################

    'geographers':[
        'You spend many days in the Library.'
        'transcribing the work of the Ancient Geographers.'
        '         You learn much'
        '         of how the world changed.'

        'Your work is not interrupted.'
    ]

# if only CW: then CW
# else if: only TB: then TB
# else: TB2

# CW = 'priests'
# TB = 'kitchens_empty'
# TB2 = 'distracted'

# TB = 'kitchens_empty'

###############################################################################################################################

}

# Break Choices #######################################################################################################
###############################################################################################################################

break_dialog = {

# 1. Young Brothers sing old songs ###############################################################################################

    'old_songs':[
        'In the kitchens, the young brothers sing'
        'XXXXX                      the old songs'
        'XXXXX                      as if they were new.'
        '                                                   '
        'Your spirit is renewed, but you lose precious time.'
    ],

# 'poets' -> here
# CW = 'playwrights'
# TB = 'drink_laugh'

# 2. Young Brothers Drink and Laugh ###############################################################################################

    'drink_laugh':[
        'In the kitchens, the young brothers drink'
        'XXXXX                           and laugh'
        'XXXXX                           as if they will live forever.'
        '                                                               '
        'Your spirit is renewed, but you lose precious time.'
    ],

# 'philophers' -> here
# CW = 'engineers'
# TB = 'small_animal'

# 3. Brothers observe small animal blessed happiness ###############################################################################################

    'small_animal':[
        'In the kitchens, the brothers observe       '
        'XXXXX                      a small animal       '
        'XXXXX                      that is blessed to bring happiness.'
        '                                                              '
        'Your spirit is renewed, but you lose precious time.'
    ],

# 'playwright' -> here
# CW = 'mystics'
# TB = 'old_songs'

# 4. Old Songs Not Forgotten ###############################################################################################

    'old_songs':[
        'In the kitchens, the brothers sing'
        'XXXXX                the old songs'
        'XXXXX                that they have not forgotten.'
        '                                                   '
        'Your spirit is renewed, but you lose precious time.'
    ],
# 'engineers' -> here
# CW = 'geographers'
# TB = 'end_is_nigh'

# 5. Old Brothers Drink End is Nigh ###############################################################################################

    'end_is_nigh':[
        'In the kitchens, the old brothers drink'
        'XXXXX                         and laugh'
        'XXXXX                         knowing the end is nigh.'
        '                                                      '
        'Your spirit is renewed, but you lose precious time.'
    ],

# CW = 'devoted'
# TB = kitchens_empty

# 7. Distracted ###############################################################################################

    'distracted':[
        'You are distracted from your work.'
        'thinking of your lost brothers'
        '         You wonder about their lives'
        '         and about your own.'
        '         You wish you were apart of theirs.'
        '                                           '
        'You search for your brothers.'
        'in the once bustling kitchens.'
    ],

# TB = 'kitchens_empty'

# 7. Kitches Empty ###############################################################################################

    'kitchens_empty':[
        'The kitchens are empty.'
        'XXXXX                  '
        'XXXXX                  '

        'You lose precious time.'
    ],

# 'geographers' -> here
# if only TB: 'reminisce'
# else: 'devoted'

# 7. Not Devoted ###############################################################################################

    'devoted':[
        'Something is missing...'
        'XXXXX                  all your work is lost'
        'XXXXX                  all your brothers are gone'
        '                                                 '
        'You have not devoted yourself towards one goal.'
    ],

# Continue -> main_menu

# 8. reminisce ###############################################################################################

    'reminisce':[
        'You reminisce on the life you once had...'
        'on the choices you made...'
        'XXXXX                the happy times were grandious'
        'XXXXX                memories of your brothers are strong'
        'XXXXX                the rewards experienced are undescribeable'
        '                                                               '
        'The memories of family bring you warmth and you are fullfiled.'
        'The memories will bring you great joy in your next life.'
        '                                                               '
        'The Great Work remains unfinished.'
    ]

# Continue -> main_menu

################################################################################################

}

# Ending Dialogue Sequence ###############################################################################################

end_dialog = {

# Preiests / Ending Sequence ###############################################################################################

    'priests':[
        'You spend many days in the Library.'
        'transcribing the work of the Ancient Priests.'
        '         You learn much'
        '         of how the Word of God was lost.'

        'Your have run out of wood for the furnace.'
        '                           You are frigid.'
    ],

# if player has axe: LWCM
# else: LW
# CW = 'cold_claims_you'
# LW = 'look'
# LWCM = 'look_cut'


# Look For Wood ###############################################################################################

    'look':[
        'XX there is no more wood XX'
        'XX nor an axe with which XX'
        'XX to cut more           XX'
    ],

# CW = 'cold_claims_you'

# Cold Claims You ###############################################################################################

    'cold_claims_you':[
        'You spend many days in the Library.'
        'until the cold claims you.'
        '         You learn much'
        '         of regret.'

        'The Great Work remains unfinished.'
    ]

# CW = restart
# TB = restart 

################################################################################################

}