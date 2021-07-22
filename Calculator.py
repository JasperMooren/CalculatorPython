import re


def calculate(string):
    if control_input(string):
        split_string = split_operation(string)
        if bool(re.search("\+", string)):
            add(split_string[0], split_string[1])
        elif bool(re.search("-", string)):
            subtract(split_string[0], split_string[1])
        elif bool(re.search("\*", string)):
            multiply(split_string[0], split_string[1])
        elif bool(re.search("/", string)):
            divide(split_string[0], split_string[1])
        else:
            print("ERROR: Code should never reach this point!")
    else:
        print("Sorry, the format is incorrect.")


def add(a, b):
    print(int(a) + int(b))


def subtract(a, b):
    print(int(a) - int(b))


def multiply(a, b):
    print(int(a) * int(b))


def divide(a, b):
    print(int(a) / int(b))


def control_input(string):
    if bool(re.match("^[0-9]{,10} ?[+\-*/] ?[0-9]{,10} {,10}$", string)):
        return True
    else:
        return False


def split_operation(string):
    split_string = re.findall("[0-9]+", string)
    # print(split_string)
    return split_string
