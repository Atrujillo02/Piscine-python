import sys


def num_characters(string):
    """
    Count the number of upper-case characters, lower-case characters,
    punctuation characters, digits, and spaces in the given string.

    Args:
        string (str): The string to analyze.

    Prints:
        The counts of each type of character in the string.
    """
    num_upper = 0
    num_lower = 0
    punctuation = 0
    num_space = 0
    num_digit = 0

    for i in string:
        if i.isupper():
            num_upper += 1
        elif i.islower():
            num_lower += 1
        elif i.isspace():
            num_space += 1
        elif i.isdigit():
            num_digit += 1
        else:
            punctuation += 1

    total_characters = len(string)
    print(f"The text contains {total_characters} characters:")
    print(f"{num_upper} upper letters")
    print(f"{num_lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{num_space} spaces")
    print(f"{num_digit} digits")


def main():
    """
    Main function to handle command-line arguments and user input.
    """

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) < 2 or sys.argv[1] is None:
            string = input("What is the text to count?\n")
            string += "\n"
        else:
            string = sys.argv[1]

        num_characters(string)

    except AssertionError as e:
        print("AssertionError:", e)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
