"""
The module provides a text-based interactive menu for navigating through HTML documentation.
"""
import os

from labs.config.paths_config import HTML_DATA
from labs.ui.menu.docs_menu import DocsMenu
from labs.ui.menu.lab2.calculator_menu import CalculatorMenu
from labs.ui.menu.lab3.ascii_art_generator_menu import AsciiArtGeneratorMenu
from labs.ui.menu.lab4.own_asscii_art_generator import OwnAsciiArtGeneratorMenu
from labs.ui.menu.lab5.figures import FigureMenu
from labs.ui.menu.lab7.user_menu import UserMenu
from labs.ui.menu.lab8.diagrams_menu import DiagramMenu

class MenuFacade:
    """
    Facade class for managing a collection of menus.

    This class provides a simple user interface to interact with a collection of menus.
    Menus are represented as tuples of menu names and menu instances. The class allows
    the user to select and execute a menu based on their choice.
    """

    EXIT_OPTION = 0

    def __init__(self):
        """
        Initialize the MenuFacade instance with a list of menus.
        """
        self.menu_options = [
            ("Calculator", CalculatorMenu()),
            ("AsciiArtGeneratorMenu", AsciiArtGeneratorMenu()),
            ("OwnAsciiArtGeneratorMenu", OwnAsciiArtGeneratorMenu()),
            ("FigureMenu", FigureMenu()),
            ("UserMenu", UserMenu()),
            ("DiagramMenu", DiagramMenu()),
            ("DocsMenu", DocsMenu(os.path.abspath(HTML_DATA)))
        ]

    def print_menu_options(self):
        """
        Print the available menu options to the console.

        This method iterates through the list of menus and prints each menu option
        along with its corresponding number.

        Returns:
            None
        """
        for index, (name, _) in enumerate(self.menu_options, start=1):
            print(f"{index}. {name}")
        print(f"{self.EXIT_OPTION}. Exit")

    def execute_selected_menu(self, choice):
        """
        Execute the selected menu based on the user's choice.

        Parameters:
            choice (int): The user's choice.

        Returns:
            bool: True if the selected menu is executed, False otherwise.
        """
        if choice == self.EXIT_OPTION:
            return True
        elif 1 <= choice <= len(self.menu_options):
            _, selected_menu = self.menu_options[choice - 1]
            selected_menu.run()
            return False
        else:
            print("Invalid choice. Enter again!")
            return False

    def start(self):
        """
        Start the menu facade, allowing the user to interact with the menus.

        This method enters a loop where it continuously prints the menu options and
        prompts the user for their choice. It then executes the selected menu.

        Returns:
            None
        """
        while True:
            self.print_menu_options()
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if self.execute_selected_menu(choice):
                    break
            except ValueError:
                print("Invalid choice. Enter again!")


if __name__ == "__main__":
    facade = MenuFacade()
    facade.start()
class MenuFacade:
    """
    Facade class for managing a collection of menus.

    This class provides a simple user interface to interact with a collection of menus.
    Menus are represented as tuples of menu names and menu instances. The class allows
    the user to select and execute a menu based on their choice.
    """

    EXIT_OPTION = 0

    def __init__(self):
        """
        Initialize the MenuFacade instance with a list of menus.
        """
        self.menu_options = [
            ("Calculator", CalculatorMenu()),
            ("AsciiArtGeneratorMenu", AsciiArtGeneratorMenu()),
            ("OwnAsciiArtGeneratorMenu", OwnAsciiArtGeneratorMenu()),
            ("FigureMenu", FigureMenu()),
            ("UserMenu", UserMenu()),
            ("DiagramMenu", DiagramMenu()),
            ("DocsMenu", DocsMenu(os.path.abspath(HTML_DATA)))
        ]

    def print_menu_options(self):
        """
        Print the available menu options to the console.

        This method iterates through the list of menus and prints each menu option
        along with its corresponding number.

        Returns:
            None
        """
        for index, (name, _) in enumerate(self.menu_options, start=1):
            print(f"{index}. {name}")
        print(f"{self.EXIT_OPTION}. Exit")

    def execute_selected_menu(self, choice):
        """
        Execute the selected menu based on the user's choice.

        Parameters:
            choice (int): The user's choice.

        Returns:
            bool: True if the selected menu is executed, False otherwise.
        """
        if choice == self.EXIT_OPTION:
            return True
        elif 1 <= choice <= len(self.menu_options):
            _, selected_menu = self.menu_options[choice - 1]
            selected_menu.run()
            return False
        else:
            print("Invalid choice. Enter again!")
            return False

    def start(self):
        """
        Start the menu facade, allowing the user to interact with the menus.

        This method enters a loop where it continuously prints the menu options and
        prompts the user for their choice. It then executes the selected menu.

        Returns:
            None
        """
        while True:
            self.print_menu_options()
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if self.execute_selected_menu(choice):
                    break
            except ValueError:
                print("Invalid choice. Enter again!")


if __name__ == "__main__":
    facade = MenuFacade()
    facade.start()
