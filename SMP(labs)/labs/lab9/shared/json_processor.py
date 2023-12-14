from colorama import Fore
from typing import Dict, Union, List
from labs.config.logger_config import logger
from labs.shared import color_processor


class JSONProcessor:
    """
    Utility class for processing JSON data.

    This class provides static methods for flattening nested JSON structures
    and displaying flattened JSON data with colored output.

    Methods:
    - flatten_json(json_data: dict, parent_key: str = '', delimiter: str = '_') -> dict:
        Flattens a nested JSON structure and returns a flattened dictionary.

    - display_flattened_json(jsons: Union[dict, List[dict]], color_position: int = 4) -> None:
        Displays flattened JSON data with colored output.

    Parameters:
    - jsons: The JSON data to be displayed (can be a dictionary or a list of dictionaries).
    - color_position (int): The position of the color in the
      color_processor.colors dictionary (default is 4).

    Raises:
    - ValueError: If data types or color position are incorrect.
    """

    @staticmethod
    def flatten_json(json_data: dict, parent_key: str = '', delimiter: str = '_') -> dict:
        """
        Flattens a nested JSON structure and returns a flattened dictionary.

        Parameters:
        - json_data (dict): The nested JSON structure to be flattened.
        - parent_key (str): The parent key used for constructing flattened
        keys (default is an empty string).
        - delimiter (str): The delimiter used between keys in the
        flattened structure (default is '_').

        Returns:
        - dict: A flattened dictionary.
        """
        if (not isinstance(json_data, dict) and not isinstance(parent_key, str)
                and not isinstance(delimiter, str)):
            raise ValueError("Incorrect data types!")

        flat_data = {}
        for key, value in json_data.items():
            new_key = parent_key + delimiter + key if parent_key else key

            if isinstance(value, dict):
                flat_data.update(JSONProcessor.flatten_json(value, new_key, delimiter))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    flat_data.update(JSONProcessor.flatten_json({str(i): item}, new_key, delimiter))
            else:
                flat_data[new_key] = value

        return flat_data

    @staticmethod
    def display_flattened_json(jsons: Union[dict, List[dict]], color_position: int = 4) -> None:
        """
        Displays flattened JSON data with colored output.

        Parameters:
        - jsons: The JSON data to be displayed (can be a dictionary or a list of dictionaries).
        - color_position (int): The position of the color in the
        color_processor.colors dictionary (default is 4).

        Raises:
        - ValueError: If data types or color position are incorrect.
        """
        if ((not isinstance(jsons, dict) or not isinstance(jsons, list))
                and not isinstance(color_position, int)):
            raise ValueError("Incorrect data types!")

        if color_position < 0 or color_position > len(color_processor.colors):
            raise ValueError("Incorrect color position!")

        if isinstance(jsons, list):
            for _, json_data in enumerate(jsons):
                flat_json = JSONProcessor.flatten_json(json_data)
                for key, value in flat_json.items():
                    print(getattr(Fore, color_processor.colors[color_position]) + f'{key}:'
                          + Fore.RESET + f' {value}')

        elif isinstance(jsons, dict):
            flat_json = JSONProcessor.flatten_json(jsons)
            for key, value in flat_json.items():
                print(getattr(Fore, color_processor.colors[color_position])
                      + f'{key}:' + Fore.RESET + f' {value}')
