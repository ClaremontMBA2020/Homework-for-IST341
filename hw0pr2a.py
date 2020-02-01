# coding: utf-8
#
# hw0pr2a.py
#

import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    user = input("Choose your weapon: ")
    comp = random.choice(['rock','paper','scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == 'rock':
        if comp == 'paper':
            print('Ha! I really chose paper--I WIN!')
            print("Better luck next time...")
        elif comp == 'rock':
            print('Oh! I chose rock too!--even!')
        else:
            print('Oh! Come on! I should not have choosed sissors.. I lost..')

    elif user == 'sissors':
        if comp == 'paper':
            print('Oh... why... I lost')
        elif comp == 'rock':
            print('Wow! Yeah -- I win!')
        else: 
            print('Oh its same choice! even!')
            
    elif user == 'paper':
        if comp == 'paper':
            print('Hey we chose same one! even!')
        elif comp =='rock':
            print('Oh... Come on! I lost..')
        else: 
            print('Haha! I won!')

    else:
        print('something is wrong! i think you did not choose neither rock, sissors and paper!! Come on Mate !')


