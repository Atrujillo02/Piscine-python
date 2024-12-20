import string
import random
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random ID for a student.

    Returns:
        str: A randomly generated ID consisting of 15 lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student with attributes such as name, surname, active status,
    login, and ID.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        active (bool): Indicates whether the student is active.
        Defaults to True.
        login (str): The student's login,
        automatically generated during initialization.
        id (str): A unique identifier for the student,
        automatically generated.
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=True, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """
        Initializes the login attribute based
        on the student's name and surname.
        The login is constructed as the first letter of the name (uppercase)
        followed by the surname in lowercase.
        """
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
