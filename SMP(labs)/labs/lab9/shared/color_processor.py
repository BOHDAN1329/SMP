import colorama
import pyfiglet
from colorama import Fore
from labs.config.logger_config import logger

colorama.init(autoreset=True)
colors = {i: color_name for i, color_name in enumerate(sorted(Fore.__dict__.keys()))}
fonts = {i: font_name for i, font_name in enumerate(sorted(pyfiglet.FigletFont.getFonts()))}

class ColorProcessor:
    @staticmethod
    def display_colors() -> None:
        """
        Displays available color options.

        Prints a numbered list of color options available in the `colors` dictionary.
        """
        logger.info("Displaying all colors")
        for i, color_name in colors.items():
            print(f"{i}. {color_name}")

class FontProcessor:
    @staticmethod
    def display_fonts() -> None:
        """
        Displays available font options.

        Prints a numbered list of font options available in the `fonts` dictionary.
        """
        logger.info("Displaying all fonts")
        for i, font_name in fonts.items():
            print(f"{i}. {font_name}")
