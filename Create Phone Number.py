# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

# мое решение

def create_phone_number(n):
    result = ["("]
    if len(n) == 10:
        for i in n:
            result.append(str(i))
            if len(result) == 4:
                result.append(") ")
            if len(result) == 8:
                result.append("-")
        return "".join(result)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# Решения других пацанов

"""
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
------------------------------------------------------------------------------------------------------------------------

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
------------------------------------------------------------------------------------------------------------------------

    def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])


  return '({}) {}-{}'.format(str1, str2, str3)
------------------------------------------------------------------------------------------------------------------------

def create_phone_number(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)
"""