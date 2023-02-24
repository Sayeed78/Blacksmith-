# Scholar_Draft_Functions.py

# Functions for Scholar ######################################################################

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