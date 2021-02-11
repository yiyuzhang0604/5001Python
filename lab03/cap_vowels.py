def convert(words):
    newWords = " "
    for letter in words:
        if letter not in "AEIOU":
            newWords = newWords + letter.lower()
        else:
            newWords = newWords + letter
    return newWords

print(convert(input("Enter any capitalized letter: ")))