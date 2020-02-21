#
# Intro to loops!
#
# Name:
#
def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
#assert fac(0) == 1
#assert fac(5) == 120

# Question 1: 
def power(b,p):
    subtotal = 0
    total = 1
    for x in range(1,p+1):     
        subtotal = b    
        total = subtotal * total
        #print("power(2, 5): should be 32 ==", total)
    return total               
    






# Question 2:
"""
Result: the sum of odd numbers in the list L.
"""
def summedOdds(L):
    result = 0
    for e in L:
        if e%2 == 0:
            result = result + e    # add only when e == odd
        else:
            result = result
    return result







# Question 3: ___________________________________________________________________________________________________________________________________________________
#def untilARepeat( high ):

import random
def countGuesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 to 99, inclusive
    numguesses = 1                           # we just made one guess, above
    while guess != hidden:
        guess = random.choice(range(0, 100)) # guess again!
        numguesses += 1                      # add one to our number of guesses
    return numguesses


#import sys
#import time
import random
# def untilARepeat(high):
#     """Uses a while loop to guess "hidden", from 0 to 99.
#        Argument: hidden, a "hidden" integer from 0 to 99.
#        Result: the number of guesses needed to guess hidden.
#     """
#     guess = random.choice(range(0, high))     # 0 to 99, inclusive
#     L = [guess]
#     numguesses = 0                           # we just made one guess, above
#     while unique(L) == True:
#         guess = random.choice(range(0, high))
#         L += [guess] # guess again!
#         numguesses += 1  
#         print(L)                    # add one to our number of guesses
#     return numguesses
    

def untilARepeat( high ):
    """ 
    makes guesses in the range(0,high) and counts the number of guesses 
    until it gets a repeat somewhere along the way...
    input: a single integer 'high' 
    output: the number of guesses needed until it gets a repeat
    """
    guess = random.choice( range(0, high) ) # 0 to 99, inclusive 
    numguesses = 0
    L = [guess]
    while unique(L) == True:
        guess = random.choice( range(0, high) ) # guess again!
        L += [guess]
        print(L) 
        numguesses += 1 # add one to our number of guesses
    return numguesses


def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])  # recursion is OK in this function!










# Draw a sample of birthdays & check if each birthday is unique

import numpy as np
def birthday_sim(people):
    simulations = 20000
    unique_birthdays = 0 
    for _ in range(simulations):
        draw = np.random.choice(365, size=23, replace=True) 
        if len(draw) == len(set(draw)): 
            unique_birthdays += 1
    out = 1 - unique_birthdays / simulations
    print(round(out*100, 5), "%")
    return out