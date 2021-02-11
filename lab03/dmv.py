import random
def licence():
    print("Welcome to the DMV (estimated wait time is 3 hours)")
    full_name = input("Please enter your first, middle, and last name:")
    last_pos = full_name.rfind(" ")
    last_name = full_name[last_pos:]
    FN = full_name[0:last_pos]
    birthdate = input("Enter date of birth (MM/DD/YY):")
    randomList = random.sample(range(0,9),7)
    licence_number = " "
    for number in randomList:
        licence_number += str(number)
    print("-------------------------------------------")
    print("Washington Drive Licence")
    print("DL",licence_number)
    print("LN",last_name)
    print("FN", FN)
    print("DOB", birthdate)
    print("EXP 05/15/21")

licence()

 