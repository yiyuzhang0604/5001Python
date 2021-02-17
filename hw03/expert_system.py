def helper():
    aching =input("Do you have aching bones or aching joints?(y/n):")
    rash = input("Do you have a rash?(y/n):")
    soreThrout = input("Do you have a sore throat?(y/n):")
    backPain =input("Do you have back pain just above the waist with chills and fever?(y/n):")
    urinatingPain =input("Do you have pain urinating or are urinating more often?(y/n):")
    sunCondition = input("Have you spent the day in the sun or in hot conditon?(y/n):")
    if aching == 'y':
        print("Possibilities include viral infection")
    elif rash == 'y':
        print("Insufficient information to list possibilities")
    elif soreThrout == 'y':
        print("Possibilities include a throat infection")
    elif backPain:
        print("Possibilities include kidney infection")
    elif urinatingPain == 'y':
        print("Possibilities include a urinary tract infection")
    elif sunCondition == 'y':
        print("Possibilities sunstroke or heat exhaustion")
    else: 
        print("Insufficient information to list possibilities")


def expertSystem():
    coughing = input("Are you coughing?(y/n):")
    shortBreath = input("Are you short of breath or wheezing or coughing up phlegm?(y/n):")
    headache =input("Do you have a headache?(y/n):")
    pain = input("Are you experiencing any of the following: pain when bending your head forward,nausea or vomitting,bright light hurting your eyes, drowsiness or confusion?(y/n):")
    vomit = input("Are you vomitting or had diarrhea?(y/n):")
    if coughing == 'y': 
        if shortBreath =='y':
            print("Possibilities include pneumonia or infection of airways")
        elif headache == 'y':
            print("Possibilities include viral infection")
        else:
            helper()
    else:
        if headache == 'y' and pain == 'y':
                print("Possibilities include menigitis")
        elif headache == 'n' and vomit == 'y':
                print("Possibilities include digestive tract infection")
        else:
            helper()

expertSystem()

