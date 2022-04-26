# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# мое решение

def pig_it(text):
    changeable_word = []
    result = []
    for i in text.split():
        if i == "?" or i == "!":
            result.append(i + " ")
        else:
            for j in i:
                changeable_word.append(j)
                if len(changeable_word) == len(i):
                    changeable_word.append(changeable_word[0])
                    changeable_word.remove(changeable_word[0])
                    changeable_word.append('ay ')
                    result.append("".join(changeable_word))
                    changeable_word.clear()
    result = "".join(result)
    l = len(result)
    result = result[:l - 1]
    return result


print(pig_it("O tempora o mores !"))

# решения других пацанов

'''
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
------------------------------------------------------------------------------------------------------------------------

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
------------------------------------------------------------------------------------------------------------------------

def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)
------------------------------------------------------------------------------------------------------------------------

import re
def pig_it(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)
------------------------------------------------------------------------------------------------------------------------
'''
