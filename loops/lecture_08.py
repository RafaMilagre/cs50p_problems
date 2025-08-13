def main():
    print_square(3)


def print_square(a):
    for i in range(a):
        print_row(a)


def print_row(l):
    print('#' * l)


main()