import pyfiglet
from colorama import Fore
import os

from labs.config.paths_config import ASCII_ART_GENERATOR
from labs.shared.color_processor import colors, fonts, FontProcessor, ColorProcessor
from labs.shared.file_processor import FileProcessor


class AsciiArtGeneratorService:
    """
    Provides a service for generating and displaying ASCII art.

    Attributes:
    - __file_processor (FileProcessor): An instance of FileProcessor for file processing.

    Methods:
    - __init__(self): Initializes an AsciiArtGeneratorService object.
    - __get_text(self, text, font, color_position, width) -> str: Generates
    formatted ASCII art text.
    - display_text(self): Takes user input to generate and display ASCII art,
     and writes it to a file.
    - get_user_input(self, prompt, input_type=int, error_message="Invalid input."): Get user input with error handling.
    - render_ascii_art(self, initial_text, font_position, color_position, width): Render and format ASCII art text.
    """

    def __init__(self):
        """
        Initializes an AsciiArtGeneratorService object.
        """
        self.__file_processor = FileProcessor()

    @staticmethod
    def __get_text(text, font, color_position, width) -> str:
        """
        Generates formatted ASCII art text.

        Parameters:
        - text (str): The input text for generating ASCII art.
        - font (str): The font style to be used for ASCII art.
        - color_position (int): The position of the color to be applied to the ASCII art.
        - width (int): The width of the ASCII art text.

        Returns:
        - str: The formatted ASCII art text.
        """
        fig = pyfiglet.Figlet(font)
        fig.width = width
        formatted_text = fig.renderText(text)
        return getattr(Fore, colors[color_position]) + formatted_text

    def get_user_input(self, prompt, input_type=int, error_message="Invalid input."):
        """
        Get user input with error handling.

        Parameters:
        - prompt (str): The prompt to display to the user.
        - input_type (type): The expected type of input.
        - error_message (str): The error message to display on invalid input.

        Returns:
        - input_type: The user-entered value of the specified type.
        """
        while True:
            try:
                user_input = input_type(input(prompt))
                return user_input
            except ValueError:
                print(error_message)

    def render_ascii_art(self, initial_text, font_position, color_position, width):
        """
        Render and format ASCII art text.

        Parameters:
        - initial_text (str): The input text for generating ASCII art.
        - font_position (int): The position of the font to be used for ASCII art.
        - color_position (int): The position of the color to be applied to the ASCII art.
        - width (int): The width of the ASCII art text.
        """
        modified_text = self.__get_text(initial_text, fonts[font_position], color_position, width)
        print(modified_text)
        self.__file_processor.write_into_file(ASCII_ART_GENERATOR, modified_text)

    def display_text(self):
        """
        Takes user input to generate and display ASCII art, and writes it to a file.

        Raises:
        - pyfiglet.CharNotPrinted: If a character is not printable in ASCII art.
        """
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            try:
                initial_text = input("Enter text containing all ASCII characters "
                                     "in order to display: ")
                if not initial_text.isascii():
                    print("Text must contain only ASCII characters")
                    continue

                FontProcessor.display_fonts()
                font_position = self.get_user_input("Enter position of font you would like to use: ")

                ColorProcessor.display_colors()
                color_position = self.get_user_input("Enter position of color you would like to use: ")

                width = self.get_user_input("Enter width of text you would like to display: ")

                self.render_ascii_art(initial_text, font_position, color_position, width)

                if input("Would you like to continue? Enter 'Y' or 'y' if you do, or "
                         "anything else if you don't. Your response is ").lower() != "y":
                    break
            except pyfiglet.CharNotPrinted as e:
                print(str(e))
            except (ValueError, KeyError):
                print("Invalid input or incorrect value for font/color.")
            else:
                break
        else:
            print(f"Exceeded maximum attempts ({max_attempts}). Exiting.")
