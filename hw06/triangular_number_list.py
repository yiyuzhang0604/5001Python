def main():
    input_line = input("Enter a number, or enter 'done':")
    answer_list = []

    while(input_line != 'done'):
        number = int(input_line)
        tri_number = int((number * (number + 1)) * 0.5)
        answer_list.append(tri_number)
        input_line = input("Enter a number, or enter 'done':")
    if(input_line == 'done'):
        print(answer_list)


main()
