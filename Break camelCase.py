# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# Моё решение

import string
def solution(s):
    result = []
    if len(s) > 1:
        for i in s:
            if i in string.ascii_uppercase:
                result.append(" " + i)
            else:
                result.append(i)
        return ''.join(result)
    else:
        return s


print(solution("camelCasing"))

# Решеия других пацанов

"""
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
------------------------------------------------------------------------------------------------------------------------

import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
------------------------------------------------------------------------------------------------------------------------

def solution(s):
    final_string = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += " " + char
        else:
            final_string += char
    return final_string
------------------------------------------------------------------------------------------------------------------------

def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr
------------------------------------------------------------------------------------------------------------------------

import re

def solution(s):
    return re.sub(r'([A-Z])', r' \1', s)
"""
