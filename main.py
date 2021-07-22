import Calculator


def main():
    print("Welcome to the Calculator!")
    print()
    while True:
        print("Please type your calculation in the following format:")
        print("[NUMBER] +|-|*|/ [NUMBER]")
        print("Then press ENTER to see the result.")
        print("If you wish to exit the Calculator, please type: EXIT")
        user_input = input()
        if user_input.upper() == "EXIT":
            break
        else:
            Calculator.calculate(user_input)


if __name__ == '__main__':
    main()
