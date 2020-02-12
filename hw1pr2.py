# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: 
# Problem description: First few functions!
from math import *

def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x




#1. Write sq(x), which accepts a numeric argument named x. Then, sq should return the square of its argument. 
def sq(x):
    """Result: sq returns squared its number
        Argument x: a number (int or float)
    """
    return x**x



#2. interp(low, hi, fraction) accepts three numbers as its arguments: low, hi, and fraction, 
    #   and should return the floating-point value that is fraction of the way between low and hi.
def interp(low, hi, fraction):
    """Result: interp returns 
    """
    return ((hi - low) * fraction + low)



#3. Write a function checkends(s), which takes in a string s and returns True if the first character in 
    #   s is the same as the last character in s. It returns False otherwise. The checkends function does not have to work on the empty string (the string '').
def checkends(s):
    """Result: 
    """
    if s[0] == s[-1] :
        return True
    else:
        return False

#4. Write a function flipside(s), which accepts a string s and returns a string whose first half is s's second half 
#   and whose second half is s's first half. If len(s) (the length of s) is odd, the "first half" of s is considered to 
# have one fewer character than the second half.
def flipside(s):
    """Result: 
    """
    x = len(s)//2
    return s[x:] + s[:x]

#5. Write convertFromSeconds(s), which takes in a nonnegative integer number of seconds s and returns a list (we'll call it L) 
#   of four nonnegative integers that represents that number of seconds in more conventional units of time
def convertFromSeconds(s):
    """Result: 
    """
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60*60)    # Number of hours
    s = s % (60*60)         # The leftover
    minutes = s // (60)     # Number of minutes
    s = s % (60)            # The leftover
    seconds = s             # Number of seconds
    return [days, hours, minutes, seconds]