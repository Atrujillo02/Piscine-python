class calculator:
    """
    Represents a calculator that can perform operations such as
    addition, multiplication, subtraction, and division on an array of numbers.
    """

    def __init__(self, object) -> None:
        """
        Initializes the calculator with an array of numbers.

        Args:
            object (list): The array of numbers.
        """
        self.array = object

    def __add__(self, object) -> None:
        """
        Adds a number to every element of the array.

        Args:
            object (int or float): The number to add.
        """
        self.array = list(map(lambda x: x + object, self.array))
        print(self.array)

    def __mul__(self, object) -> None:
        """
        Multiplies a number with every element of the array.

        Args:
            object (int or float): The number to multiply.
        """
        self.array = list(map(lambda x: x * object, self.array))
        print(self.array)

    def __sub__(self, object) -> None:
        """
        Subtracts a number from every element of the array.

        Args:
            object (int or float): The number to subtract.
        """
        self.array = list(map(lambda x: x - object, self.array))
        print(self.array)

    def __truediv__(self, object) -> None:
        """
        Divides every element of the array by a number.

        Args:
            object (int or float): The number to divide by.

        Raises:
            ZeroDivisionError: If the divisor is zero.
        """
        try:
            self.array = list(map(lambda x: x / object, self.array))
            print(self.array)
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
