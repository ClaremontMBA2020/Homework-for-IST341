# coding: utf-8
#
# hw0pr2.py
#

import time          # includes a library named time
import random        # includes a library named random


def rps():
    """ This plays a game of rock-paper-scissors
        (or a variant of that game ...)
        arguments: no argument (prompted text doesn't count as an argument)
        results: no results    (printing doesn't count as a result)
    """
    name = input('Hi...what is your name? ')
    print()
    print("Hmmm...")
    print()

    if name == 'Eliot' or name == 'Ran':
        print('I\'m "offline" Try later.')
        
    elif name == 'Zach':
        print('Efron?')
        time.sleep(.25)
        print('No?')
        time.sleep(.25)
        print('Mmm')
        
    else:
        print('Welcome,', name)
        my_choice = random.choice(['rock','paper','scissors'])
        print('By the way, I choose ', my_choice)