import os
import colorama
from colorama import Fore
import re
from functools import reduce

colorama.init(autoreset=True)
colors = {i: getattr(Fore, color) for i, color in enumerate(sorted(Fore.__dict__.keys()))}


class DataProcessor:

    def __init__(self, file_path):
        if file_path is None:
            raise ValueError("File path should have a value")
        self.__file_path = file_path

    def _read_file(self):
        with open(self.__file_path, "r") as file:
            return file.read()

    @staticmethod
    def display_colors():
        for i, color in colors.items():
            print(f"{i}. {color}")

    @staticmethod
    def _parse_metadata(line, meta_data):
        if not re.match(r"^\w+::\d+$", line):
            raise ValueError("Metadata has incorrect format")
        key, value = line.split("::")
        meta_data[key] = int(value)

    @staticmethod
    def _process_data_annotation(line, meta_data, is_data_annotation_found):
        if line == "@data":
            if "height" not in meta_data:
                raise ValueError("The file has to contain meta information such as height")
            is_data_annotation_found[0] = True

    def _get_all_data(self):
        file_data = self._read_file().split("\n")
        is_data_annotation_found = [False]
        representation = ""
        symbol = None

        for line in file_data:
            self._process_data_annotation(line, self.__meta_data, is_data_annotation_found)

            if is_data_annotation_found[0]:
                if re.match("^@symbol::.$", line):
                    if symbol is not None:
                        self.__data[symbol] = representation
                    symbol = line[9:]
                    representation = ""
                    length = 0
                    counter = 1
                elif re.match(r"^\^.+\$$", line):
                    if counter == 1:
                        length = len(line)
                    if len(line) != length:
                        raise ValueError("Length of the row has to be equal within a certain character in the file")
                    representation += line[1:-1] + ("" if counter == self.__meta_data["height"] else "\n")
                    counter += 1
                else:
                    raise ValueError("Data information has incorrect format")

            elif not is_data_annotation_found[0]:
                self._parse_metadata(line, self.__meta_data)

    def retrieve(self, text, color_position, width):
        result = {}
        all_needed_symbols = {}
        properties = {}
        row_count = 0
        current_position_in_row = 0

        for i in range(len(text)):
            representation = str(self.__data[text[i]]).split("\n")
            if current_position_in_row + len(representation[0]) > width:
                if len(representation[0]) > width:
                    raise ValueError("Width of the text is too small")
                row_count += 1
                current_position_in_row = 0
                current_position_in_row += len(representation[0])
                properties[row_count] = properties.get(row_count, 0) + 1
            else:
                current_position_in_row += len(representation[0])
                properties[row_count] = properties.get(row_count, 0) + 1
            all_needed_symbols.update({i: reduce(lambda x, y: x + "\n" + y, representation)})

        symbol_count = 0
        for i in properties:
            for j in range(properties[i]):
                representation = all_needed_symbols[symbol_count].split("\n")
                symbol_count += 1
                for k in range(len(representation)):
                    result[k + i * 6] = result.get(k + i * 6, "") + representation[k]

        return colors[color_position] + reduce(lambda x, y: x + "\n" + y, result.values())


class TxtProcessor(DataProcessor):
    __meta_data = {}
    __data = {}

    def __init__(self, file_path):
        if not file_path.endswith(".txt") and os.path.exists(file_path):
            raise ValueError("File should be .txt file")
        super().__init__(file_path)
        self._get_all_data()
