import sys

def check_odd_even(num: int) -> None:
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"

    if len(sys.argv) == 2:
        int_arg = int(sys.argv[1])
        check_odd_even(int_arg)

except AssertionError as e:
    print("AssertionError:", e)
except ValueError:
    print("AssertionError: argument is not an integer")