import random
def guessing():
    print("Welcome to the Guessing Game!\nI picked a number between 1 and 50. Try and guess!")
    answer = random.randint(1,50)
    print(answer)
    guess1 = input("Enter your guess:")
    tries = 1
    while int(guess1)!= answer:
        if abs(answer-int(guess1)) <= 1:
            print("Your guess is scalding hot")
            guess1 = input("Enter your guess:")
        elif abs(answer - int(guess1)) <= 2:
            print("Your guess is extremely warm")
            guess1 = input("Enter your guess:")
        elif abs(answer - int(guess1))<=3:
            print("Your guess is very warm")
            guess1 = input("Enter your guess:")
        elif abs(answer - int(guess1)) <= 5:
            print("Your guess is warm")
            guess1 = input("Enter your guess:")
        elif abs(answer - int(guess1)) <= 8:
            print("Your guess is cold")
            guess1 = input("Enter your guess:")
        elif abs(answer - int(guess1)) <= 13:
            print("Your guess is very cold")
            guess1 = input("Enter your guess:")
        elif abs(answer - int(guess1)) <= 20:
            print("Your guess is extremely cold")
            guess1 = input("Enter your guess:")
        elif abs(answer - int(guess1)) > 20:
            print("Your guess is icy freezing miserably cold")
            guess1 = input("Enter your guess:")
        tries += 1

    if int(guess1) == answer:
        print("Congraguation! You figured it out in", tries, "tries")
    
    if tries == 1:
        print("That was lucky!")
    elif tries >= 2 and tries <= 4:
        print("That was amazing!")
    elif tries >=5 and tries <=6:
        print("That was okay.")
    elif tries == 7:
        print("Meh.")
    elif tries >= 8 and tries <= 9:
        print("This is not your game.")
    elif tries >= 10:
        print("You are the worest guesser I've ever seen.")
guessing()
