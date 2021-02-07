def expertSystem():
    coughing = bool(input("Are you coughing:"))
    shortBreath = bool(input("Are you short of breath or wheezing or coughing up phlegm:"))
    headache = bool(input("Do you have a headache:"))
    pain = bool(input("Are you experiencing any of the following: pain when bending your head forward,nausea or vomitting,bright light hurting your eyes, drowsiness or confusion:"))
    vomit = bool(input("Are you vomitting or had diarrhea:"))
    aching = bool(input("Do you have aching bones or aching joints:"))
    rash = bool(input("Do you have a rash:"))
    soreThrout = bool(input("Do you have a sore throat:"))
    backPain = bool(input("Do you have back pain just above the waist with chills and fever:"))
    urinatingPain = bool(input("Do you have pain urinating or are urinating more often:"))
    sunCondition = bool(input("Have you spent the day in the sun or in hot conditon:"))
    if coughing: 
        if shortBreath:
            print("Possibilities include pneumonia or infection of airways")
        else:
            if headache:
                print("Possibilities include viral infection")
            else:
                if aching: 
                    print("Possibilities include viral infection")
                else:
                    if rash: 
                        print("Insufficient information to list possibilities")
                    else:
                        if soreThrout:
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

