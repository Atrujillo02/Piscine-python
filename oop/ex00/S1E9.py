from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class representing a character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initializes a character with a name and a health state.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Specifies if the character is alive.
            Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Changes the health state of the character.
        This method must be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    Represents a member of the Stark family.
    """

    def die(self):
        """
        Changes the health state of the character to deceased.
        """
        self.is_alive = False
