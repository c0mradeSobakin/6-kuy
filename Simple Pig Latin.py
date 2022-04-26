# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    changeable_word = []
    result = []
    for i in text.split():
        if len(i) == 1:
            result.append(i)
            continue
        for j in i:
            changeable_word.append(j)
            if len(changeable_word) == len(i):
                changeable_word.append(changeable_word[0])
                changeable_word.remove(changeable_word[0])
                changeable_word.append('ay ')
                result.append("".join(changeable_word))
                changeable_word.clear()
    return "".join(result)


print(pig_it("Pig latin is cool"))
