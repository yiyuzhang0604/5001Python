import math
def drawCircle():
    radius = int(input("Enter the radius:"))
    if(radius < 0 ):
        print("Invalid input")
        return
    
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius+1):
            if(math.sqrt(x*x + y*y))<= radius:
                print('o', end = "")
            else:
                print(' ', end = "")
        print()

drawCircle()