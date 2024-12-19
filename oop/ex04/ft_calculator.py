class calculator:
    """
    Represents a calculator that can perform operations such as
    addition, multiplication, and subtraction on arrays of numbers.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and prints the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        array_vec = [int(V1[i] * V2[i]) for i in range(len(V1))]
        print(f"Dot Product is: {sum(array_vec)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the addition of two vectors and prints the result.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        array_vec = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is: {array_vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the subtraction of two vectors and prints the result.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        array_vec = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {array_vec}")
