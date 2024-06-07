import logging
import os


class File:
    """
    Represents a file on the filesystem.

    Args:
        filepath (str): The path to the file.

    Attributes:
        filepath (str): The path to the file.

    Methods:
        exists: Checks if the file exists.
        readlines: Reads all lines from the file.

    """

    def __init__(self, filepath):
        self.filepath = filepath

    def exists(self) -> bool:
        """
        Checks if the file exists.

        Returns:
            bool: True if the file exists, False otherwise.

        """
        logging.debug(f"Checking if file exists: {self.filepath}")
        return os.path.exists(self.filepath)

    def readlines(self, bypass_errors=True) -> list:
        """
        Reads all lines from the file.

        Returns:
            list: A list of strings representing the lines in the file.

        """
        if not self.exists():
            logging.error(f"File not found: {self.filepath}")
            if bypass_errors:
                logging.warning("Bypassing errors and returning an empty list")
                return []
            raise FileNotFoundError(f"File not found: {self.filepath}")
        with open(self.filepath, "r") as f:
            logging.debug(f"Reading lines from file: {self.filepath}")
            return f.readlines()
