def validator():
    number = []
    print("Enter a magic number:")
    for i in range(0,3):
        element = input()
        number.append(element)
    
    converter = 1 
    for i in range(0,3):
        rsum = 0
        for j in range(0,3):
            rsum = rsum + int(number[i][j])
        if(rsum != 15):
           converter = 0; 
    
    for i in range(0,3):
        csum = 0
        for j in range(0,3):
            csum = csum + int(number[j][i])
        if(csum != 15):
            converter = 0
    
    mdsum = 0
    for i in range(0,3):
        mdsum = mdsum + int(number[i][i])
    if(mdsum != 15):
        converter = 0
    
    odsum = 0
    for i in range(0,3):
        odsum = odsum + int(number[i][2-i])
    if(odsum != 15):
        converter = 0

    if converter == 1: 
        print("This is a magic square!")
    else:
        print("Not a magic square!")

validator()
