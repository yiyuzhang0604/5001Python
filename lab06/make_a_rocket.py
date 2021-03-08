import sys


def main():
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    try:
        striped = sys.argv[3]
    except IndexError:
        striped = False

    if(striped == False):
        if(width % 2 == 0):
            even_built(width, height, False)
        else:
            odd_built(width, height, False)
    else:
        if(width % 2 == 0):
            even_built(width, height, True)
        else:
            odd_built(width, height, True)


def odd_built(width, height, striped):
    for i in range(1, width - 1, 2):
        for j in range(0, (width - i)//2):
            print(" ", end="")
        for k in range(0, i):
            print("*", end="")
        for j in range(0, (width - i)//2):
            print(" ", end="")
        print("", end="\n")
    for k in range(0, height):
        if (striped):
            for i in range(0, width // 2):
                for j in range(0, width):
                    print("_", end="")
                print("", end="\n")
            for i in range(0, (width + 1) // 2):
                for j in range(0, width):
                    print("X", end="")
                print("", end="\n")
        else:
            for i in range(0, width):
                for j in range(0, width):
                    print("X", end="")
                print("", end="\n")
    for i in range(width // 2, width + 1, 2):
        for j in range(0, (width - i)//2):
            print(" ", end="")
        for j in range(0, i):
            print("*", end="")
        for j in range(0, (width - i)//2):
            print(" ", end="")
        print("", end="\n")
    for j in range(0, width):
        print("*", end="")
    print("", end="\n")


def even_built(width, height, striped):
    for i in range(2, width - 1, 2):
        for j in range(0, (width - i)//2):
            print(" ", end="")
        for k in range(0, i):
            print("*", end="")
        for j in range(0, (width - i)//2):
            print(" ", end="")
        print("", end="\n")
    for k in range(0, height):
        if (striped):
            for i in range(0, width // 2):
                for j in range(0, width):
                    print("_", end="")
                print("", end="\n")
        for i in range(0, (width + 1) // 2):
            for j in range(0, width):
                print("X", end="")
            print("", end="\n")
    for i in range(width // 2, width + 1, 2):
        for j in range(0, (width - i)//2):
            print(" ", end="")
        for j in range(0, i):
            print("*", end="")
        for j in range(0, (width - i)//2):
            print(" ", end="")
        print("", end="\n")
    for j in range(0, width):
        print("*", end="")
    print("", end="\n")


main()
