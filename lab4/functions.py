import os
import pyfiglet
from colorama import Fore, Style

def create_art():
    text = input("Enter your phrase: ")
    font = input("Choose font style (standard, slant, shadow, etc.): ")
    color = input("Choose text color (red, blue, green, etc.): ")
    width = int(input("Enter width of ASCII art: "))
    height = int(input("Enter height of ASCII art: "))
    characters = input("Enter characters to use (default: '@#*'): ") or "@#*"
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        colored_art = f"{Fore.__dict__[color.upper()]}{ascii_art}{Style.RESET_ALL}"
        scaled_art = "\n".join([line.center(width) for line in colored_art.splitlines()]).splitlines()
        final_art = "\n".join(["".join([char for char in line]) for line in scaled_art])
        return final_art, characters
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Function to save ASCII art to a file
def save_to_file(art, characters):
    filename = input("Enter the name of the file to save the art: ")
    try:
        with open(f"{filename}.txt", "w") as file:
            file.write("\n".join([line.replace("@", characters[0]).replace("#", characters[1]).replace("*", characters[2]) for line in art.splitlines()]))
        print(f"ASCII art saved to {filename}.txt")
    except Exception as e:
        print(f"Error: {e}")

# Function to view ASCII art from files
def view_art():
    try:
        files = sorted([file for file in os.listdir() if file.endswith('.txt')])
        for idx, file in enumerate(files):
            print(f"{idx + 1}. {file}")
        file_number = int(input("Enter the number of the file you want to view: ")) - 1
        with open(files[file_number], "r") as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error: {e}")

# Function to delete ASCII art files
def delete_art():
    try:
        files = sorted([file for file in os.listdir() if file.endswith('.txt')])
        for idx, file in enumerate(files):
            print(f"{idx + 1}. {file}")
        file_number = int(input("Enter the number of the file you want to delete: ")) - 1
        file_name = files[file_number]
        os.remove(file_name)
        print(f"{file_name} deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")