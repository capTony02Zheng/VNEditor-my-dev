import configparser
from utils.file_utils import *
from .Exception import *


class Loader:
    """
    config loading helper
    """

    def __init__(self, config_dir: str):
        if check_file_valid(config_dir):
            self.config = configparser.ConfigParser()
            self.config.read(config_dir)
        else:
            raise ConfigLoaderError("cannot open config file")

    def game_memory(self) -> dict:
        return dict(self.config["GameMemory"])

    def engine(self) -> dict:
        return dict(self.config["Engine"])

    def log_file(self) -> dict:
        return dict(self.config["LogFile"])

    def resources(self) -> dict:
        return dict(self.config["Resources"])

    def register_service(self) -> dict:
        return dict(self.config["RegisterService"])

    def version(self) -> dict:
        return dict(self.config["Version"])

    def get_all_section(self) -> list:
        """

        :return: get all sections in config file
        """
        return list(self.config.sections())
