import json
import pandas as pd
from labs.config.logger_config import logger

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

class FileProcessor:
    """
    FileProcessor is a class that interacts with files for reading and writing.
    """

    @staticmethod
    def write_into_file(file_path: str, text: str) -> None:
        """
        Write text into a file. May raise PermissionError or OSError.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            logger.info("Writing into file %s", file_path)
            file.write(text)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Read text from a file. May raise FileNotFoundError, PermissionError, or OSError.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            logger.info("Reading from file %s", file_path)
            return file.read()

    @staticmethod
    def read_from_json(file_path: str) -> dict:
        """
        Read a JSON file. May raise FileNotFoundError, PermissionError, OSError, or JSONDecodeError.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            logger.info("Reading from file %s", file_path)
            return json.load(file)

    @staticmethod
    def write_into_json(file_path: str, jsons: list) -> None:
        """
        Write a JSON text into a file. May raise FileNotFoundError, PermissionError, OSError, or JSONDecodeError.
        """
        if not isinstance(file_path, str):
            logger.critical("Wrong data type: %s. It has to be string!", type(file_path))
            raise TypeError("Type of file_path must be string")
        if not isinstance(jsons, list):
            logger.critical("Wrong data type: %s. It has to be list!", type(jsons))
            raise TypeError("Type of jsons must be list")

        jsons_text_representation = json.dumps(jsons, indent=4)
        json.loads(jsons_text_representation)

        with open(file_path, "w", encoding="utf-8") as file:
            logger.info("Writing into file %s", file_path)
            file.write(jsons_text_representation)


class CsvProcessor:
    """
    CsvProcessor is used to interact with csv-files.
    """

    @staticmethod
    def read(file_path: str) -> pd.DataFrame:
        """
        Read a CSV file into a pandas DataFrame. May raise FileNotFoundError, PermissionError, or OSError.
        """
        if not isinstance(file_path, str):
            logger.critical("Wrong data type: %s. It has to be string!", type(file_path))
            raise TypeError("Type of file_path must be string")
        return pd.read_csv(file_path)
