# Scholar_Draft 

def scholar_text():
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('XX THE BLOOD OF SCHOLARS X')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
        #time.sleep(2)
        print('X SHALL OUTWEIGTH XXXXXXXX')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('XX THE BLOOD OF MARTYRS XX')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
        print()
        #time.sleep(2)
        print('You are Arkady')
        #time.sleep(.5)
        print('        the Scholar')
        #time.sleep(.5)
        print('        the Chronicler')
        #time.sleep(.5)
        print('        the Sage')
        print('')
        #time.sleep(1)
        print('XX The world has been consumed by ice. XXXX')
        #time.sleep(1)
        print('XX In the Last Monastery XXXXXXXXXXXXXXXXXX')
        #time.sleep(1)
        print('XX of the land of Faith, XXXXXXXXXXXXXXXXXX')
        #time.sleep(1)
        print('XX you complete the thoughts of the dead XX')
        #time.sleep(1)
        print('XXXXXXX that God might know who they were X,')
        #time.sleep(1)
        print()
        print('The hazy ghost of Weariness is always upon you, breaking your will. ')
        print('You fear that you may fail before the Great Work is finished.')
        print()
        



# Func goes through y/n work loop
def work():
        g2g = 0
        dialog(1, 'Work')
        print()
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

# Func creates contiune working segment break
def cont_work():
        dialog(1, 'Continue working')
        print()
        answer = input('You must keep working ')
        return answer

# Func goes through work/break dialog loop
def work_break():
        g2g = 0
        dialog(1, 'Continue working')
        dialog(2, 'Take a break')
        print()
        answer = input('Choice? ')
        if answer == '1' or '2':
                return answer
                print()
        else:
                wrong_answer()
                return work_break()

# Func goes through work/look for wood dialog tree
def work_wood():
        dialog(1, 'Continue working')
        dialog(2, 'Look for wood')
        print()
        answer = input('Choice? ')
        if answer == '1':
                print()
        elif answer == '2':
                if item_check(axe) != 1:
                               print('XX there is no more wood XX')
                               print('XX nor an axe with which XX')
                               print('XX to cut more           XX')
                               print()
                               cont_work()
                       
                       
                else:
                        wrong_answer()
                        return work_wood()

# Great Work unfinished ending Function
def work_unfinished():
        print('You spend many days in the Library,')
        print('until the cold claims you.')
        print('     You learn much')
        print('     of regret.')
        print()
        print('The Great Work remains unfinished.')
        print()
                       
# This pulls up the scholar path of the game
# A list is created to determine choices 
def scholar():
        scholar_list = []
        work_choice_results = 0
        scholar_text()
#        read_line_fast("scholar.txt")
        work()
        print()
        print('You spend many days in the Library.')
        #time.sleep(.5)
        print('transcribing the work of the Ancient Poets.')
        print('         You learn much')
        print('         of thier dedication to the Sublime.')
        #time.sleep(.5)
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
                print()
                work_break()
                if answer == '2':
                        print('In the kitchens, the young brothers drink')
                        print('XXXXX                           and laugh')
                        print('XXXXX                           as if they will live forever.')
                        print()
                        print('Your spirit is renewed, but you lose precious time.')
                        print()
                        work_break()
                        if answer == '2':
                                print('You spend many days in the library,')
                                print('transcribing the work of the Ancient Engineers.')
                                print('         You learn much')
                                print('         of how the world was made.')
                                print()
                                print('Your work is interrupted by a monk:')
                                print('Come, brother! Let us sing the old songs once more!')
                                print()
                                if answer == '2':
                                        print('In the kitchens, the brothers sing')
                                        print('XXXXX                the old songs')
                                        print('XXXXX                that they have not forgotten.')
                                        print()
                                        print('Your spirit is renewed, but you lose precious time.')
                                        print()
                                        work()
                                        if answer == '2':
                                                print('In the kitchens, the young brothers drink')
                                                print('XXXXX                           and laugh')
                                                print('XXXXX                           as if they will live forever.')
                                                print()
                                                print('Your spirit is renewed, but you lose precious time.')
                                                print()
                                                cont_work()
                                                print('You spend many days in the Library.')
                                                print('transcribing the work of the Ancient Geographers.')
                                                print('         You learn much')
                                                print('         of how the world changed.')
                                                print()
                                                print('Your work is not interrupted.')
                                                print()
                                                work_break()
                                                if answer == '2':
                                                        print('The kitchens are empty.')
                                                        print('XXXXX                  ')
                                                        print('XXXXX                  ')
                                                        print()
                                                        print('You lose precious time.')
                                                        print()
                                                        cont_work()
                                                        print('You spend many days in the Library.')
                                                        print('transcribing the work of the Ancient Priests.')
                                                        print('         You learn much')
                                                        print('         of how the Word of God was lost.')
                                                        print()
                                                        print('Your have run out of wood for the furnance.')
                                                        print('                           It is very cold.')
                                                        print()

        
        elif answer == '2':
                print()
                
        print('In the kitchens, the young brothers sing       ')
        print('XXXXX                      the old songs       ')
        print('XXXXX                      as if they were new.')
        print()
        print('Your spirit is renewed, but you lose precious time.')
        print()
        cont_work()
        print()
        print('You spend many days in the Library.')
        print('transcribing the work of the Ancient Playwrights.')
        print('         You learn much')
        print('         of of the human paradox.')
        print()
        print('Your work is interrupted by a monk:')
        print('"Come, brother! We have discovered a strange miricle!"')
        print()
        answer = work_break()
        if answer == '1':
                work_choice_results += 1
                print('You spend many days in the Library.')
                print('transcribing the work of the Ancient Engineers')
                print('         You learn much')
                print('         of how the world was made.')
                print()
                print('Your work is interrupted by a monk:')
                print('"Come, brother! Let us sing the old songs once more!"')
                print()
                work_break()
                if answer == '1':
                        work_choice_results += 1
                        print('You spend many days in the Library.')
                        print('transcribing the work of the Ancient Mystics')
                        print('         You learn much')
                        print('         of what the ancients feared.')
                        print()
                        print('Your work is interrupted by an old monk:')
                        print('"Come, brother! We have opened the last barrel of wine!"')
                        print()
                        work_break()
                        if answer == '1':
                                work_choice_results += 1
                                print('You spend many days in the Library.')
                                print('transcribing the work of the Ancient Geographers')
                                print('         You learn much')
                                print('         of how the world changed.')
                                print()
                                print('Your work is not interrupted.')
                                print()
                                work_break()
                                if answer == '1':
                                        work_choice_results += 1
                                        print('You spend many days in the Library.')
                                        print('transcribing the work of the Ancient Priests')
                                        print('         You learn much')
                                        print('         of how the Word of God was lost.')
                                        print()
                                        print('You have run out of wood for the furnance.')
                                        print('                          It is very cold.')
                                        print()
                                        work_wood()
                        
                                                        
        elif answer == '2':
                print('In the kitchens, the brothers observe       ')
                print('XXXXX                      a small animal       ')
                print('XXXXX                      that is blessed to bring happiness.')
                print()
                print('Your spirit is renewed, but you lose precious time.')
                print()
                work()
        print
##################################################################################################