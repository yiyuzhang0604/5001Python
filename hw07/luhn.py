# Name: Yiyu Zhang
# Github: https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-YiyuZhang/tree/master/hw07

def main():
    take_input()


def take_input():
    number = input("Enter a number:")
    original_list(number)


def original_list(number):
    """ read the list from right to left"""
    number_list = []
    for i in number[::-1]:
        digit = int(i)
        number_list.insert(0, digit)
    double(number_list)


def double(number_list):
    """ double the certain digit, and save it in the new list """
    length = len(number_list)
    i = length - 1
    double_list = []
    DOUBLE = 2
    while i >= 0:
        if(length % 2 == 0):
            if(i % 2 == 0):
                double_digit = number_list[i] * DOUBLE
                double_list.insert(0, double_digit)
            else:
                double_list.insert(0, number_list[i])
        else:
            if(i % 2 != 0):
                double_digit = number_list[i] * DOUBLE
                double_list.insert(0, double_digit)
            else:
                double_list.insert(0, number_list[i])
        i -= 1
    convert(double_list)


def convert(double_list):
    """ creating a new list """
    answer_list = []
    for j in double_list:
        if(j // 10 >= 1):
            digit1 = j % 10
            digit2 = (j//10) % 10
            new_number = digit1 + digit2
            answer_list.append(new_number)
        else:
            answer_list.append(j)

    validate(answer_list)


def validate(answer_list):
    """ check if the number is valid"""
    total = 0
    for j in answer_list:
        total += j

    if(total % 10 == 0):
        print("The number is valid.")
    else:
        print("The number is not valid.")


main()
