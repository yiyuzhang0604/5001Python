import math 
def main():
    x1 = input("Enter x1:")
    x2 = input("Enter x2:")
    y1 = input("Enter y1:")
    y2 = input("Enter y2:")
    pow1 = math.pow((int(x1)-int(x2)),2)
    pow2 = math.pow((int(y1)-int(y2)),2)
    distance = round(math.sqrt((pow1+pow2)),2)
    print("Distance:", distance)

main()
