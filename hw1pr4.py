#
# example script to...
#

# read in a file
FILENAME = "Greta.txt"   # variables are our friends!

f = open(FILENAME, "r", encoding="utf-8")    # open FILENAME for reading
data = f.read()            # data holds all of the file's data (a big string)

# print to make sure we see what we expect!
#print(data[:42])           # first 20 characters

# split all the data into a list of words
LoW = data.split()         # LoW is a variable ("list of words")

# print to make sure we see what we expect!
#print(LoW[0:5])            # first five words (note: they are "words"!)


# exit - for now - we can always comment this out!
import sys
#sys.exit(0)                # this is Python's "system exit" 

# LOOP!

# our goal is to build intuition about how loops work
# so, we will have the script print things in detail

# this loops through each word in the LoW
# it adds 1 if the word begins with a 'D'
# we start our count at 0
count = 0

"""
theword = input("Please enter a charater that you want to explore:\n")
"""



from string import ascii_lowercase
for i in ascii_lowercase : 
    theword = i
    wordlist = []
    
    for word in LoW:           # the loop variable, word, takes each value!

#    print("word is", word, end=' & ')   # print word, followed by ' & '

        if word[0] == theword:     # if the current word starts with 'D'
            count = count + 1  # add 1 to count


### after the loop is complete, we can print the total number of the word been used:
#    print("")
#    print("After looking at every word, the # of words starting with ", theword)
#    print("is,", count)
    count = 0
#this loop would find how many target words has been used in the context:
    for word in LoW:           # the loop variable, word, takes each value!
        if word[0] ==  theword:     # if the current word starts with 'D'
            wordlist.append(word[:40])  # add 1 to count
        
### after the loop is complete, we can print the total number of target word:
#    print("\n The words with ", theword)
#    print("are these -> ", wordlist)


#most frequently used word
    from collections import Counter
    print("")
    max_word_dict = dict(Counter(wordlist))
#    if len(max_word_dict) != 0:
#        print(max(max_word_dict, key=max_word_dict.get), " is the most frequently used in this word list")
#    elif len(max_word_dict) == 0:
#        print(theword, " is not used ")

wordlist_2 =[]
for z in ascii_lowercase : 
    theword_2 = z    
    for word in LoW:           # the loop variable, word, takes each value!
        if word[0] == theword_2:     # if the current word starts with 'D'
            count = count + 1  # add 1 to count
    count = 0
    for word in LoW:           # the loop variable, word, takes each value!
        if word[0] ==  theword_2:     # if the current word starts with 'D'
            wordlist_2.append(word[:40])  # add 1 to count
    from collections import Counter

max_word_dict = dict(Counter(wordlist_2))
print(max(max_word_dict, key=max_word_dict.get), " is the most frequently used in this entire list of words")
    
if max(max_word_dict, key=max_word_dict.get) == "the":
    print("The person might likely to emphasize language !!")
else:
    print("I need to think something else")


from string import ascii_uppercase
for x in ascii_uppercase : 
    theword = x
    wordlist = []
    
    for word in LoW:           # the loop variable, word, takes each value!

#    print("word is", word, end=' & ')   # print word, followed by ' & '

        if word[0] == theword:     # if the current word starts with 'D'
            count = count + 1  # add 1 to count


### after the loop is complete, we can print the total number of the word been used:
#    print("After looking at every word, the # of words starting with ", theword)
#    print("is,", count)
    

    count = 0
#this loop would find how many target words has been used in the context:
    for word in LoW:           # the loop variable, word, takes each value!
        if word[0] ==  theword:     # if the current word starts with 'D'
            wordlist.append(word[:40])  # add 1 to count
from collections import Counter
print("")
max_word_dict = dict(Counter(wordlist))

wordlist_2 =[]
for y in ascii_uppercase : 
    theword_2 = y    
    for word in LoW:           # the loop variable, word, takes each value!
        if word[0] == theword_2:     # if the current word starts with 'D'
            count = count + 1  # add 1 to count
    count = 0
    for word in LoW:           # the loop variable, word, takes each value!
        if word[0] ==  theword_2:     # if the current word starts with 'D'
            wordlist_2.append(word[:40])  # add 1 to count
    from collections import Counter

max_word_dict = dict(Counter(wordlist_2))

print(max(max_word_dict, key=max_word_dict.get), " is the most frequently used in this entire list of upper words")
if max(max_word_dict, key=max_word_dict.get) == "I":
    print("The person might likely to express own feeling !!")
else:
    print("I need to think something else")


"""
Questions!

1. What are the first 42 characters of sanders.txt?
I don’t have to tell anybody here that we 


2. What are the first five words of sanders.txt?
['I', 'don’t', 'have', 'to', 'tell']


3. What are the first 84 characters of sanders.txt?
I don’t have to tell anybody here that we are living in a dangerous and unprecedente


4. What are the 42nd, 43rd, and 44th words of sanders.txt?
are

5. Repeat the above questions for trump.txt
    1. Thank you very much. Thank you. Thank you
    2. ['Thank', 'you', 'very', 'much.', 'Thank']
    3. Thank you very much. Thank you. Thank you very much. Madam Speaker, Mr. Vice Presid
    4. ver

6. How many words in sanders.txt start with 'D'?
7


7. How many words in sanders.txt start with 'd'?
178

8. How many words in trump.txt start with 'R'?  How about 'r'?
R = 8
r = 67


9. Create a file of your own (by grabbing text from the web).
created Greta.txt

10. Answer the above questions (1-8) for your file.
    1. My message is that we'll be watching you.
    2. 'My', 'message', 'is', 'that', "we'll"]
    3. My message is that we'll be watching you. This is all wrong. I shouldn't be up here
    4. T
    6. 0
    7. 13
    8. 1, 9


11. Choose your own question to answer using this type of analysis.
    It can be sophisticated, serious, silly, ... anything.

Share your question - and answer - here:

My analysis would illustrate which word has been used with specific character, and show which word was most frequently said in list of the words. 
And so, I might be able to get idea of what kind of person the speaker is. 

Leave your source code (above) as it was to answer your own question!

Great work!  This is the process by which any computational question
  - about any set of data at all - is tackled. Much more in the future!

"""