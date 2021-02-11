def expertSystem():
    coughing = input("Are you coughing:")
    shortBreath = input("Are you short of breath or wheezing or coughing up phlegm:")
    headache =input("Do you have a headache:")
    pain = input("Are you experiencing any of the following: pain when bending your head forward,nausea or vomitting,bright light hurting your eyes, drowsiness or confusion:")
    vomit = input("Are you vomitting or had diarrhea:")
    aching =input("Do you have aching bones or aching joints:")
    rash = input("Do you have a rash:")
    soreThrout = (input("Do you have a sore throat:")
    backPain =input("Do you have back pain just above the waist with chills and fever:")
    urinatingPain =input("Do you have pain urinating or are urinating more often:")
    sunCondition = input("Have you spent the day in the sun or in hot conditon:")
    if coughing == 'yes' or 'Yes' or 'y' or'Y': 
        if shortBreath =='yes' or 'Yes' or 'y' or'Y':
            print("Possibilities include pneumonia or infection of airways")
        else:
            if headache == 'yes' or 'Yes' or 'y' or'Y':
                print("Possibilities include viral infection")
            else:
                if aching == 'yes' or 'Yes' or 'y' or'Y':
                    print("Possibilities include viral infection")
                else:
                    if rash == 'yes' or 'Yes' or 'y' or'Y':
                        print("Insufficient information to list possibilities")
                    else:
                        if soreThrout == 'yes' or 'Yes' or 'y' or'Y':
                            print("Possibilities include a throat infection")
                        else:
                            if backPain:
                                print("Possibilities include kidney infection")
                            else:
                                if sunCondition:
                                    print("Possibilities sunstroke or heat exhaustion")
                                else: 
                                    print("Insufficient information to list possibilities")
    else:
        if headache:
            if pain:
                print("Possibilities include menigitis")
            else:
                if vomit:
                    print("Possibilities include digestive tract infection")

expertSystem()

