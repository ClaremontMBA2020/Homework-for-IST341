# coding: utf-8
#
# hw0pr2b.py
#

""" 
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.

"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 0.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    username = input("What is your name ? ")

    print()
    print("Welcome,", username, " to the AI Investment lab")
    print("Let's explore what type of investment strategy is suitable for you!")
    print()

    investmentexperience = int(input("How many years of investment experience do you have? [please put positive numbers]"))
    if investmentexperience != 0:
            print("well, it is good that you have experience!")
    

    howmanytimes = input("how frequent would you like to invest in a week? [1/10/100/more]")
    if howmanytimes == "1":
        print("ok! let me come back somtimes to give you advice!")
    elif howmanytimes == "10":
        print("about average parson. let's discuss how to manage your portfolio1")
    elif howmanytimes == "100":
        print("ok. you might be a daytrader! I am excited to help you!")
    else:
        print("Are you a professional investor? I might not be able to help you much, but let me try my best!")


    print("Your quest: understand your investment risk tolerance")
    print()
    Risk = input("What Risk level would you prefer? [High, Medium, Low]")
    if Risk == "Medium":
        print("Wise! You will take most well balanced portfolio.")
    elif Risk == "High":
        print("I guess" , username, "prefer adventure! Let us help you to survive in changing environment.")
    else:
        print("Understand. You are conservative and It is good thing in this rapidly changing world")
    print()

    print("Let's get on to the quest!\n\n")
    print("There are some two-bagger, ten-bagger, to one side,")
    print("Composite Indixies that benchimarking financial market, to the other,")
    print("It is all your decision!.")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose the individual stocks or the indixies? [stock/index] ")
    print()

    if choice1 == "stock":
        print("It is risky, but you can manage risk by diversifying numbers of stocks.")
        print("Please tell me more about what types of investor you are.")
        time.sleep(delay)
        
        stockchoice = input("would you like to invest in advanced economy or emerging market? [advance/emerging]")
        if stockchoice == "advance":
            print("You might be from United States")
            print("We would prepare suitable stocks for you!!")
            print("Go well,", username, "!")
        else:
            print("I see, you are curious about global development and hungry for return! Let us help you to explore growing market!!")
            print("Go well,", usename, "!")

    elif choice1 == "index":
        print("You are trendy person and chose the most popular investment vehicle!")
        print("Index is more efficient for managing your wealth!")
        time.sleep(delay)
    
        print("But, there are still many choices ahead,", username, "tell us more of your preference?")
        indexchoise = input("would you like to invest in advanced economy or emerging market? [advance/emerging]")
        if indexchoise == "advance":
                print("GOOD! you are well knowledged investor. I am happy to serve you!")
                print("Let's follow market and believe in our economy.")
        else:
                print("Nice! you are sophisticated investor!")
                print("you definately need our assistance if you want to survive in emerging market investment!")


    else:
        print("I think you did not type properly, please start again from begining !")

    