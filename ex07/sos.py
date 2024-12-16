import sys


NESTED_MORSE = {
    " ": "/ ",      "A": ".- ",
    "B": "-... ",   "C": "-.-. ",
    "D": "-.. ",    "E": ". ",
    "F": "..-. ",   "G": "--. ",
    "H": ".... ",   "I": ".. ",
    "J": ".--- ",   "K": "-.- ",
    "L": ".-.. ",   "M": "-- ",
    "N": "-. ",     "O": "--- ",
    "P": ".--. ",   "Q": "--.- ",
    "R": ".-. ",    "S": "... ",
    "T": "- ",      "U": "..- ",
    "V": "...- ",   "W": ".-- ",
    "X": "-..- ",   "Y": "-.-- ",
    "Z": "--.. ",   "0": "----- ",
    "1": ".---- ",  "2": "..--- ",
    "3": "...-- ",  "4": "....- ",
    "5": "..... ",  "6": "-.... ",
    "7": "--... ",  "8": "---.. ",
    "9": "----. "
}

def string_to_morse(str):
    """
    This function converts a string to Morse code.

    Parameters:
        str: The string to convert.

    Returns:
        str: The Morse code of the given string.
    """
    morse_list = []

    for char in str:
        morse_list.append(NESTED_MORSE[char])
    
    return ''.join(morse_list)  



def main():
    """
    This function is the main function of the program.
    It takes a single string as an argument and converts it to Morse code.
    """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        input_str = sys.argv[1]
        assert all(char.isalnum() or char == ' ' for char in input_str), "the arguments are bad"
        input_str = input_str.upper()
        assert all(char in NESTED_MORSE for char in input_str), "the arguments are bad"
        print(string_to_morse(input_str))
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()