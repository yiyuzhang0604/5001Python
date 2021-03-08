def main():
    n = input_size()
    print_cube(n)


def input_size():
    n = int(input("Input cube size(multiple of 2):"))
    return n


def print_cube(n):
    corner = "+"
    horizontal = "-"
    vertical = "|"
    slash = "/"
    space = " "
    new_line = "\n"

    h_number = 2 * n
    v_number = n
    s_number = int(n/2)

    boundry = corner + horizontal * h_number + corner
    top_view = space * (s_number + 1) + boundry + new_line
    front_view = vertical + space * h_number + vertical

    j = s_number
    i = ""
    while j:
        top_view += space * j + slash + h_number * space + \
                    slash + space * (s_number - j) + vertical + new_line
        j -= 1
        i += front_view + space*j + slash + new_line

    print(top_view + boundry + space * s_number + vertical)
    print((front_view + space * s_number + vertical + new_line) *
          (s_number - 1) + front_view + space*s_number+corner)
    print(i + boundry)


main()
