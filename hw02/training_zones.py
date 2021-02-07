def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")
    maxHR = round(208 - 0.7* age,2)
    reserveHR = maxHR - restHR
    z1low = round(restHR + reserveHR*0.5, 2)
    z1high = round(restHR + reserveHR* 0.6,2)
    z2high = round(restHR + reserveHR*0.7,2)
    z3high = round(restHR + reserveHR* 0.8,2)
    z4high = round(restHR + reserveHR* 0.93,2)
    z5high = round(restHR + reserveHR,2)
    print("Your heart rate reserve is:", str(reserveHR),"bpm")
    print("Here is a breakdown of your trianing zones: \nZone 1:",str(z1low), "to", str(round(z1high-0.01,2)),
        "bpm\nZone 2:",str(z1high),"to",str(round(z2high-0.01,2)),"bpm\nZone 3:",str(z2high),"to",str(round(z3high-0.01,2)),
        "bpm\nZone 4:",str(z3high),"to",str(round(z4high-0.01,2)),"bpm\nZone 5:",str(z4high),"to",str(z5high),"bpm")

    print("=======================================")

main()
