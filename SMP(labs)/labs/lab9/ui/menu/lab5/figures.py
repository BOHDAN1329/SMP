from labs.config.paths_config import FIGURE_2D, FIGURE_3D
from labs.service.lab5.figures_service import Figure3D, Cube
from labs.shared.color_processor import colors, ColorProcessor
from labs.shared.file_processor import FileProcessor
from labs.ui.menu_builder import Menu


class FigureMenu(Menu):
    """A menu class for managing 3D figures and their representations."""

    def __init__(self):
        """Initialize the FigureMenu."""
        self.__is_figure_available = False
        self.__is_2d_representation_available = False
        self.__is_3d_representation_available = False
        self.__figure = None
        self.__representation_2d_file = FIGURE_2D
        self.__representation_3d_file = FIGURE_3D

    def __create_cube(self):
        """Create a cube based on user input."""
        character = self.__get_character_input()
        print("There are such colors available:")
        ColorProcessor.display_colors()
        color_position = self.__get_color_position_input()
        length = self.__get_length_input()

        try:
            self.__figure = Cube(length, character, color_position)
            self.__is_figure_available = True
        except ValueError as e:
            print(f"Error: {e}")
            self.__is_figure_available = False

    def __display_2d(self):
        """Display the 2D representation of the figure."""
        if self.__is_figure_available:
            representation_2d = self.__figure.get_2d_representation()
            for item in representation_2d:
                print(item)
            self.__is_2d_representation_available = True
        else:
            print("There is no figure available!")

    def __display_3d(self):
        """Display the 3D representation of the figure."""
        if self.__is_figure_available:
            representation_3d = self.__figure.get_3d_representation(scale=self.__get_scale_input())
            print(representation_3d)
            self.__is_3d_representation_available = True
        else:
            print("There is no figure available!")

    def __save_representation(self, representation, file_path, description):
        """Save the representation of the figure to a file."""
        if representation:
            try:
                FileProcessor.write_into_file(file_path, "".join(representation))
                print(f"{description} representation saved successfully.")
            except (PermissionError, FileNotFoundError) as e:
                print(f"Error while saving {description} representation: {e}")
        else:
            print("There is no figure available!")

    def __get_character_input(self):
        """Get a character input for representing the shape."""
        while True:
            character = input("Enter a character to represent in the shape: ")
            if Figure3D.is_appropriate_character(character):
                return character
            print("Invalid character. Please enter one character.")

    def __get_color_position_input(self):
        """Get a color input for representing the shape."""
        while True:
            try:
                color = int(input("Enter a number of color: "))
                if color in range(len(colors)):
                    return color
                print("Invalid color option. Please enter a valid color number.")
            except ValueError:
                print("Invalid input. Please enter an integer number.")

    def __get_length_input(self):
        """Get a length input for creating a cube."""
        while True:
            try:
                length = int(input("Enter a length: "))
                if length > 0:
                    return length
                print("Invalid length. Please enter a length greater than 0.")
            except ValueError:
                print("Invalid input. Please enter an integer number.")

    def __get_scale_input(self):
        """Get a scale input for displaying 3D representations."""
        while True:
            try:
                scale = float(input("Enter a scale for figure: "))
                if scale > 0:
                    return scale
                print("Invalid scale. Please enter a scale greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a float number.")

    def run(self):
        """Run the FigureMenu program."""
        while True:
            print("1 - Create a cube")
            print("2 - Display 2D")
            print("3 - Display 3D")
            print("4 - Save 2D")
            print("5 - Save 3D")
            print("0 - Exit")
            option = input("Enter an option: ")

            match option:
                case "1":
                    self.__create_cube()
                case "2":
                    self.__display_2d()
                case "3":
                    self.__display_3d()
                case "4":
                    self.__save_representation(
                        self.__figure.get_2d_representation(),
                        self.__representation_2d_file,
                        "2D"
                    )
                case "5":
                    self.__save_representation(
                        self.__figure.get_3d_representation(scale=self.__get_scale_input()),
                        self.__representation_3d_file,
                        "3D"
                    )
                case "0":
                    break
                case _:
                    print("Invalid option!")
