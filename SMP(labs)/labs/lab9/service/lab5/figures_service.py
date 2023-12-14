from abc import ABC, abstractmethod
from colorama import Fore
from labs.shared.color_processor import colors

class Figure3D(ABC):
    """
    An abstract class for 3D figures.

    Attributes:
    - _character (str): The character representing the figure.
    - _color_position (int): The position of the color to be applied to the figure.

    Methods:
    - __init__(self, character: str, color_position: int): Initializes a Figure3D object.
    - get_2d_representation(self) -> list: Abstract method to get the 2D representation of the figure.
    - get_3d_representation(self) -> str: Abstract method to get the 3D representation of the figure.
    - is_appropriate_character(character: str) -> bool: Static method to check if the character is appropriate.
    """

    def __init__(self, character: str, color_position: int):
        """
        Initializes a Figure3D object.

        Parameters:
        - character (str): The character representing the figure.
        - color_position (int): The position of the color to be applied to the figure.
        """
        if color_position not in colors:
            raise ValueError("Color position must be in range of available colors")
        if not self.is_appropriate_character(character):
            raise ValueError("Only one character is allowed")
        self._character = character
        self._color_position = color_position

    @abstractmethod
    def get_2d_representation(self) -> list:
        """
        Abstract method to get the 2D representation of the figure.

        Returns:
        - list: A list containing the 2D representation of the figure.
        """
        pass

    @abstractmethod
    def get_3d_representation(self) -> str:
        """
        Abstract method to get the 3D representation of the figure.

        Returns:
        - str: The 3D representation of the figure.
        """
        pass

    @staticmethod
    def is_appropriate_character(character: str) -> bool:
        """
        Static method to check if the character is appropriate.

        Parameters:
        - character (str): The character to be checked.

        Returns:
        - bool: True if the character is appropriate, False otherwise.
        """
        return len(character) == 1

class Cube(Figure3D):
    """
    Represents a 3D cube.

    Attributes:
    - __length (int): The length of the cube.
    - __offset (int): The offset for cube representation.

    Methods:
    - __init__(self, length: int, character: str, color_position: int): Initializes a Cube object.
    - get_2d_representation(self) -> list: Gets the 2D representation of the cube.
    - get_3d_representation(self, scale: float = 1.0) -> str: Gets the 3D representation of the cube.

    Example:
    >>> cube = Cube(3, "*", 1)
    >>> cube.get_3d_representation()
    '3D representation of the cube with color applied.'
    """

    def __init__(self, length: int, character: str, color_position: int):
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        super().__init__(character, color_position)
        self.__length = length

    def get_2d_representation(self) -> list:
        """
        Gets the 2D representation of the cube.

        Returns:
        - list: A list of 2D representations of the cube.
        """
        result = ""
        for row in range(self.__length):
            for col in range(self.__length):
                result += f"{self._character}  " if row == 0 or row == self.__length - 1 or col == 0 or col == self.__length - 1 else "   "
            result += "\n"

        return [f"{Fore.__getattribute__(colors[self._color_position])}\n{result}" for _ in range(6)]

    def get_3d_representation(self, scale: float = 1.0) -> str:
        """
        Gets the 3D representation of the cube.

        Parameters:
        - scale (float): The scaling factor for the cube representation.

        Returns:
        - str: The 3D representation of the cube with color applied.
        """
        modified_length = max(int(self.__length * scale), 2)
        modified_offset = int(modified_length / 2 + 1)
        result = ""

        for row in range(modified_offset - 1):
            for col in range(modified_length + modified_offset - 1):
                result += f"{self._character}" + ("  " if col != modified_length + modified_offset - 2 or row != 0 else "")
            result += "\n"

        for row in range(modified_length):
            for col in range(modified_length + modified_offset):
                if (row == 0 or row == modified_length - 1 or col == 0 or col == modified_length - 1) and col < modified_length or \
                        (row + col == (modified_length - 1) * 2 and col < modified_length + modified_offset - 1):
                    result += f"{self._character}" + ("  " if row != modified_length - 1 or col != modified_length - 1 else "")
                elif row < modified_length - modified_offset and col > modified_length:
                    result += f"{self._character}" if col == modified_offset + modified_length - 1 else "   "

            result += "\n"

        return f"{Fore.__getattribute__(colors[self._color_position])}\n{result}"
