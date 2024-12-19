from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """

    def __init__(self, first_name: str):
        """
        Initializes a member of the Baratheon family.

        Args:
            first_name (str): The first name of the character.
        """
        super().__init__(first_name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Returns the string representation of the instance.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __repr__(self):
        """
        Returns the string representation of the instance.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def die(self):
        """
        Marks the character as not alive.
        """
        self.is_alive = False


class Lannister(Character):
    """
    Representing the Lannister family.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initializes a member of the Lannister family.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Specifies if the character is alive.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Returns the string representation of the instance.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __repr__(self):
        """
        Returns the string representation of the instance.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def die(self):
        """
        Marks the character as not alive.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        """
        Creates a Lannister character instance with a custom is_alive status.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool): Specifies if the character is alive.

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        instance = cls(first_name, is_alive)

        return instance
