import math
def main():
    angle =input("Enter an angle:")
    cosine = math.cos(math.radians(int(angle)))
    sine = math.sin(math.radians(int(angle)))
    print("The sine of", str(angle),"is",str(sine))
    print("The cosine of", str(angle),"is",str(cosine))

main()