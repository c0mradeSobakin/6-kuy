# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
#
# Examples:
#             spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
#             spinWords( "This is a test") => returns "This is a test"
#             spinWords( "This is another test" )=> returns "This is rehtona test"

# Мое решение
def spin_words(sentence):
    result = []
    text = sentence.split()
    for i in text:
        if len(i) >= 5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)


print(spin_words("This is another test"))

# Решение других пацанов
'''
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
-----------------------------------------------------------------------------------------------------------------------

def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)
-----------------------------------------------------------------------------------------------------------------------

def spin_words(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())
-----------------------------------------------------------------------------------------------------------------------

def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string
-----------------------------------------------------------------------------------------------------------------------
import re

def spin_words(sentence):
    # Your code goes here
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)
'''
