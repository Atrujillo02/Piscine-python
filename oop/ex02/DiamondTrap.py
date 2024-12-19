from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    The mad King himself.
    """

    def __init__(self, first_name):
        """
        Initializes the King class.
        Inherits from both Baratheon and Lannister.

        Args:
            first_name (str): The first name of the King.
        """
        super().__init__(first_name)

    @property
    def eyes(self):
        """
        Retrieves the color of the King's eyes.

        Returns:
            str: The color of the eyes.
        """
        return self.eyes

    @eyes.setter
    def eyes(self, color):
        """
        Sets the color of the King's eyes.

        Args:
            color (str): The new eye color.
        """
        self.eyes = color

    @property
    def hairs(self):
        """
        Retrieves the color of the King's hairs.

        Returns:
            str: The color of the hairs.
        """
        return self.hairs

    @hairs.setter
    def hairs(self, color):
        """
        Sets the color of the King's hairs.

        Args:
            color (str): The new hair color.
        """
        self.hairs = color
