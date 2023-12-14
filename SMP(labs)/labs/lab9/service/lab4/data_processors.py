from colorama import Fore
from functools import reduce
import os
import re
from abc import ABC, abstractmethod

from labs.shared.color_processor import colors


class DataProcessor(ABC):
    """Abstract base class for processing data from text files."""

    def __init__(self, file_path):
        if not file_path or not file_path.endswith(".txt") or not os.path.exists(file_path):
            raise ValueError("Invalid file path")
        self.__file_path = file_path

    @abstractmethod
    def _get_all_data(self) -> None:
        """Abstract method to retrieve all data from the file."""

    @abstractmethod
    def retrieve(self, text, color_position, width) -> str:
        """Abstract method to retrieve formatted text representation."""

    def _read_file(self) -> str:
        """Read the contents of the file."""
        with open(self.__file_path, "r", encoding="utf-8") as file:
            return file.read()


class TxtProcessor(DataProcessor):
    """Implementation class for processing data from text files with a .txt extension."""
    __meta_data = {}
    __data = {}

    def __init__(self, file_path):
        super().__init__(file_path)
        self._get_all_data()

    def _get_all_data(self) -> None:
        file_data = self._read_file().split("\n")
        is_data_annotation_found = False
        representation = ""
        symbol = None

        for line in file_data:
            if is_data_annotation_found:
                if re.match("^@symbol::.$", line):
                    if symbol is not None:
                        self.__data[symbol] = representation
                    symbol = line[9:]
                    representation = ""
                    length = 0
                    counter = 1
                elif re.match("^\\^.+\\$$", line):
                    if counter == 1:
                        length = len(line)
                    if len(line) != length:
                        raise ValueError("Length of the row has to be equal within a certain character in the file")
                    representation += line[1:-1] + ("" if counter == self.__meta_data["height"] else "\n")
                    counter += 1
                else:
                    raise ValueError("Data information has incorrect format")
            elif line == "@data":
                if "height" not in self.__meta_data:
                    raise ValueError("The file has to contain meta information such as height")
                is_data_annotation_found = True
            elif not is_data_annotation_found:
                if re.match("^\\w+::\\d+$", line):
                    key, value = line.split("::")
                    self.__meta_data[key] = int(value)
                else:
                    raise ValueError("Metadata has incorrect format")

    def retrieve(self, text, color_position, width) -> str:
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
            all_needed_symbols[i] = reduce((lambda x, y: x + "\n" + y), representation)

        symbol_count = 0
        for i in properties:
            for _ in range(properties[i]):
                result.setdefault(k := i * 6 + symbol_count, "").join(all_needed_symbols[k])
                symbol_count += 1

        return getattr(Fore, colors[color_position]) + reduce((lambda x, y: x + "\n" + y), result.values())
