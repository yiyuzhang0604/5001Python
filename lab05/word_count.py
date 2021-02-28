import re

def main():
    filename = input("Enter the file name:")
    try:
        f = open(filename,"r")
    except FileNotFoundError as e:          ## avoid crashing,
        print("Can't open", filename)
        return
 
    ## count the words and characters
    words_count = 0
    char_count = 0
    digit = 0

    test = re.compile('\w')
    text = f.read()
    words_count = len(text.split())
    char_count = len(''.join(text.split()))
    digit = len(test.findall(text))
    
    print("Words:",words_count)
    print("Characters:",char_count)
    print("Letters and numbers:",digit)
   
main()