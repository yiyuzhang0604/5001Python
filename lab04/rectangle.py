def drawRect():
    symbol = input("Pick one of the character (&,#,+,n,s,3):")
    width= int(input("Enter width:"))
    height = int(input("Enter height:"))
    if(width < 2 or height < 2):
        print("The value is too small!")

    for i in range(1,height+1):
        for j in range(1,width+1):
            if(i == 1 or i == height or j == 1 or j == width):
                print(symbol,end = "")
            else:
                print(end = ' ')
        print(end="\n\n")

drawRect()