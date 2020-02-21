# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name:
# Problem description: Sleepwalking student
import random  
def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

# __________________Quesrtion 1 ______________________________

from random import choice
def copyrs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return choice([-1, 1])
# __________________Quesrtion 1 ______________________________




# # example "random" code from class
# #
# import sys
# sys.setrecursionlimit(50000) # extra stack room
# import time
# from random import *

# def guess(hidden):
#     """A number-guessing example
#        to highlight using the
#        random library
#     """
#     comp_guess = choice(range(100)) # 0 to 99, incl.

#     if comp_guess == hidden:
#         print("I got it! It was", comp_guess)
#         print("Total guesses:")
#         return 1

#     else:
#         print("Aargh. I guessed", comp_guess)
#         time.sleep(0.1)
#         return 1 + guess(hidden)




# __________________Quesrtion 2 ______________________________
import numpy as np
from random import *
def rwpos(start, nsteps):
    """
    Return: find how many times of getting answer with random within target steps
    """
    i = 0
    L = [1, -1]
    while i != nsteps:
        start = start + np.random.choice(L)
        i += 1
    
    print("Position is  ", start)
    
# __________________Quesrtion 2 ______________________________


# __________________Quesrtion 3 ______________________________
# A character that changes depending on whether it's moving left or right 
import sys
import time
import random
def rwsteps(start, low, hi):
    run = 0
    sys.setrecursionlimit(50000)
    
    if start == low or start == hi:
        return True
    else:
        run = rs()
        if run >=0:
            start = start + run
            print('|'+' '*(start - low)+'(~‾▿‾)~'+' '*(hi - start)+'|') # A character that changes depending on whether it's moving left or right 
            sys.stdout.flush()   
            time.sleep(0.1)     
            rest_of_steps = rwsteps(start,low,hi) + 1
        else: 
            start = start + run
            print('|'+' '*(start - low)+'~(‾▿‾~)'+' '*(hi - start)+'|') # A character that changes depending on whether it's moving left or right 
            sys.stdout.flush()   
            time.sleep(0.1)     
            rest_of_steps = rwsteps(start,low,hi) + 1
        return rest_of_steps
# __________________Quesrtion 3 ______________________________

# __________________Quesrtion 4 ______________________________
# reference to https://github.com/jeffrey-xiao/harvey-mudd-college-introduction-to-python/blob/master/H3_P3.py
def rwposPlain(start, nsteps):
    """
    Return: 
    """
    newstart = start
    if nsteps == 0:
        return newstart
    return rwposPlain(newstart + rs(), nsteps-1)

def ave_signed_displacement (numtrials):
    sum = 0;
    for x in range(numtrials):
        sum += rwposPlain(0, 100)
    return sum / numtrials
def ave_squared_displacement (numtrials):
    sum = 0;
    for x in range(numtrials):
        sum += rwposPlain(0, 100)**2
    return float(sum) / numtrials
# __________________Quesrtion 4 ______________________________