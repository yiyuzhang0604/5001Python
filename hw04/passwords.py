## Name: Yiyu Zhang
## Description: this program takes in users' full name and favorite word, and automatically generate 3 passwords for the users 
import random
def generator():
    print("Welcome to the username and password generator!")
    fname = input("Please enter your first name:")
    lname = input("Please enter your last name:")
    word = input("Please enter your favorite word:")
    # generate a random number for creating user name 
    rnumber = str(random.randint(0,100))
    #start generating the user name 
    # first check the lenghth of the last name, if less than 7, add * to the end 
    if(len(lname)<7):
        new_lname = lname + "*"* (7-int(len(lname)))
    else:
        new_lname = lname[0:6]

    user = fname[0]+new_lname+rnumber
    print("") ## print a new line to seperate the sections 

    print("Thanks",fname,",","your user name is",user)
    print("")
    # first password
    # using a for loop, to iterate through the full name, and convert the character one by one. At the end, convert the list into string 
    fnumber = str(random.randint(0,100))
    name_list = []
    full_name = str.lower(fname+lname)
    for i in range(0,len(full_name)):
        if(full_name[i] == 'a'):
            name_list.append('@')
        elif(full_name[i] == 'o'):
            name_list.append('0')
        elif(full_name[i] == 'l'):
            name_list.append('1')
        elif(full_name[i] == 's'):
            name_list.append('$')
        else:
            name_list.append(str.lower(full_name[i]))
    
    name_list.insert(len(fname),fnumber) #insert the number between first name and last name 
    str1 = ""

    # second password 
    # using slicing to retrive the first and last character of every required word
    second_ps = str.lower(fname[0])+str.upper(fname[len(fname)-1])+str.lower(lname[0])+str.upper(lname[len(lname)-1])+str.lower(word[0])+str.upper(word[len(word)-1])

    #thir password

    f_len = len(fname)
    l_len = len(lname)
    w_len = len(word)
    new_len1 = random.randint(1,f_len)
    new_len2 = random.randint(1,l_len)
    new_len3 = random.randint(1,w_len)
    third_ps = fname[0:new_len1]+lname[0:new_len2]+word[0:new_len3]


    print("Here are three suggested passwords for you to consider:")
    print("")
    print("Password 1:", str1.join(name_list))
    print("Password 2:", second_ps)
    print("Password 3:", third_ps)

generator()
