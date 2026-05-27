import os
import yaml


class ConfigLoader:

    def __init__(self, env):

        file_path = f"config/{env}.yaml"

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Config file not found: {file_path}"
            )

        with open(file_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self, section, key):

        try:
            return self.config[section][key]

        except KeyError:
            raise KeyError(
                f"Missing config value: [{section}] -> {key}"
            )