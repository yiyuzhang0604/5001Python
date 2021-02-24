import sys
if __name__ == "__main__":
    n = int(sys.argv[1])
    seq=[]
    n1, n2 = 0, 1
    count = 0
    while count < n:
        seq.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

    print(seq)