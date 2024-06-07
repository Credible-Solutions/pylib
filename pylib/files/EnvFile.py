import logging
import os

from pylib.files.File import File


class EnvFile(File):
    def __init__(self, filepath: str):
        logging.debug(f"Creating EnvFile object with filepath: {filepath}")
        super().__init__(filepath)

    def set_env_variabes(self, bypass_errors=True) -> int:
        """
        Sets environment variables based on the contents of the file.

        Reads each line from the file, strips any leading or trailing whitespace,
        and checks if the line is a comment or does not contain an equal sign.
        If the line is a valid key-value pair, it sets the environment variable
        using the key-value pair.

        Note: This method assumes that the file contains key-value pairs in the
        format 'key=value'.

        Returns:
            int: 0 if the method doesn't set any value.
        """
        count = 0
        lines = self.readlines(bypass_errors=True)
        for line in lines:
            logging.debug(f"Processing line: {line}")
            line = line.strip()
            if line.startswith("#") or not line or "=" not in line:
                continue
            key, value = line.split("=", 1)
            logging.debug(f"Setting environment variable: {key}={value}")
            os.environ[key] = value
            count += 1
        logging.debug(f"Set {count} environment variables")
        return count


if __name__ == "__main__":
    print("11")
    env_file = EnvFile(filepath=".env")
    print(env_file.set_env_variabes(bypass_errors=True))
