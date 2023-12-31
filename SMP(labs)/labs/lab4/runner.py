from functions import *


def write_into_file(file_path, text):
    with open(file_path, "w") as file:
        file.write(text)


def read_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    try:
        initial_text = input("Enter text in order to display: ")
        DataProcessor.display_colors()
        color_position = int(input("Enter position of color you would like to use: "))
        width = int(input("Enter width of text you would like to display: "))
        file_path = input("Enter path to file containing alphabet: ")

        txt_processor = TxtProcessor(file_path)
        text = txt_processor.retrieve(initial_text, color_position, width)

        print(text)
        write_into_file("output.txt", text)

    except KeyError as e:
        print(f"Key error! {e}")
    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print("File not found! Please, check the path to the file")


if __name__ == "__main__":
    main()
