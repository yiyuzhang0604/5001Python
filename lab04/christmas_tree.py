def drawTree():
    width = int(input("Enter the width of the tree:"))
    valid = False
    if(width % 2 != 0):
        valid = True
    else:
        print("The input is not valid.")
        width = int(input("Please enter an odd number:"))
        if(width % 2 == 0):
            valid = True
        
    
    if(valid == True):
        print("")
        top = (width//2)+1
        for i in range(1,width+1):
            if(i == top):
                print("*", end = "")
            else:
                print(" ",end = "")
        print("")

        height = (width // 2)+1
        remain = height - 2
        for i in range(1,remain+1):
            for j in range(1,width+1):
                if(j == top - i):
                    print("/", end = "")
                elif(j == top + i):
                    print("\\", end = "")
                else:
                    print(" ", end = "")
            print("")
    
        for i in range(1,width+1):
            if (i == 1):
                print("/",end = "")
            elif(i == width):
                print("\\", end = "")
            else:
                print("_",end = "")
                  
    else:
        print("Sorry can't print the tree")
    
    print("\n")

drawTree()