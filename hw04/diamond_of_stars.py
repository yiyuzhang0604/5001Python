import sys
if __name__ == "__main__":
    width = int(sys.argv[1])
    i = 1
    if (width % 2 == 0):
        width = width - 1
        time = 1
    else:
        time = 0
    while (i < width):
        x = 0
        j = 0
        while (j < (width - i) / 2):
            j += 1
            print(' ', end="")
        while (x < i):
            print('*', end="")
            x += 1
        while (j >= 1):
            j -= 1
            print(' ', end="")
        print('\n')
        i += 2

    while (time >= 0):
        c = 0
        while (c < width):
            print('*', end = "")
            c += 1
        print('\n')
        time -= 1
    i -= 2
    while (i > 0):
        f = 0
        y = 0
        while (f < (width - i) / 2):
            f += 1
            print(' ', end = "")
        while (y < i):
            print('*', end = "")
            y += 1
        while (f >= 1):
            f -= 1
            print(' ', end="")
        print('\n')
        i -= 2
        


    




