import sys
import os
import yaml
from typing import Dict, List

# Example class demonstrating OOP concepts in Python
class GlobalParams(dict):
    def __init__(self) -> None:
        # Initialize the dictionary and update it with the YAML file contents
        super().__init__()
        self.update(self.get_yml_file())

    @staticmethod
    def get_yml_file() -> Dict:
        """
        Static method to read and return the contents of a YAML file.
        This method does not depend on the instance of the class (no 'self' used).
        """
        # Get the last command line argument, assuming it's the YAML file name
        file_name = sys.argv[-1]

        # Default to 'config.yml' if the file name does not contain '.yml'
        if ".yml" not in file_name:
            file_name = "config.yml"

        # Check if the file exists
        if os.path.isfile(file_name):
            with open(file_name) as file:
                data = yaml.load(file, Loader=yaml.FullLoader)
            return data

        # Raise an error if the file is not found
        raise FileNotFoundError(f"{file_name} config file is not available")

    @property
    def database_meta(self) -> Dict[str, str]:
        """
        Property to return a dictionary containing database metadata.
        This method uses 'self', hence it operates on the instance level.
        """
        db_string: str = self.get("DB_URL")
        buffer: List[str] = db_string.split("/")
        second_buffer: List[str] = buffer[-2].split(":")
        third_buffer: List[str] = second_buffer[1].split("@")
        return {
            "DB_URL": db_string,
            "DB_NAME": buffer[-1],
            "DB_USER": second_buffer[0],
            "DB_PASSWORD": third_buffer[0],
            "DB_LOCATION": f"{third_buffer[1]}:{second_buffer[-1]}",
        }

# Example usage of the GlobalParams class
if __name__ == "__main__":
    try:
        # Create an instance of GlobalParams
        params = GlobalParams()
        print("Database Metadata:")
        print(params.database_meta)
    except Exception as e:
        print(e)

# Singleton implementation using metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Example singleton class
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Example usage of the SingletonClass
if __name__ == "__main__":
    singleton1 = SingletonClass("first")
    singleton2 = SingletonClass("second")

    print("Singleton values:")
    print(singleton1.value)  # Output: first
    print(singleton2.value)  # Output: first (since it's the same instance)
