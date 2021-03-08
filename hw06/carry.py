def main():
    first = int(input("Enter the first numbers:"))
    second = int(input("Enter the second numbers:"))
    add(first, second)


def add(digit1, digit2):
    carry = 0
    count = 0
    number_list = []
    d1 = digit1
    d2 = digit2
    while(d1 != 0 or d2 != 0):
        if(d1 == 0 and d2 != 0):
            new2 = d2 % 10
            new_digit = int((new2 + carry) % 10)
            number_list.append(new_digit)
            carry = (new2 + carry)//10
            d2 = d2 // 10
        elif(d1 != 0 and d2 == 0):
            new1 = d1 % 10
            new_digit = int((new1 + carry) % 10)
            number_list.append(new_digit)
            carry = (new1 + carry)//10
            d1 = d1 // 10
        else:
            new1 = d1 % 10
            new2 = d2 % 10
            new_digit = int((new1 + new2 + carry) % 10)
            number_list.append(new_digit)
            carry = (new1 + new2)//10
            d1 = d1 // 10
            d2 = d2 // 10
        if(carry != 0):
            count += 1

    if(carry != 0):
        number_list.append(1)
    combine(digit1, digit2, number_list, count)


def combine(digit1, digit2, number_list, count):
    ans = 0
    list.reverse(number_list)

    length = len(number_list)
    for i in range(0, length):
        if (i == 0):
            d = number_list[i]
            ans += d * (pow(10, length-1))
        else:
            if(number_list[i] != 0):
                d = number_list[i]
                ans += (pow(10, length - i-1)) * d

    print(digit1, "+", digit2, "=", ans)
    print("Number of carries: ", count)


main()
