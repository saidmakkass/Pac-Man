import json
from typing import List
from pydantic import BaseModel, model_validator


class DataValidator(BaseModel):
    highscore_filename: str
    lives: int
    pacgum: int
    points_per_pacgum: int
    points_per_super_pacgum: int
    points_per_ghost: int
    level_max_time: int
    levels: List

    @model_validator(mode="after")
    def validate_config(self):
        self.highscore_filename = self.highscore_filename.strip()
        if not self.highscore_filename.endswith(".json"):
            raise ValueError(
                "Invalid highscore_filename: "
                "filename must end with '.json'"
            )

        return self


class Parser:
    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path
        self.validated_config = None

    def get_config(self):
        with open(self.config_file_path, "r") as config_file:
            config_content = config_file.read()

        clean_lines = []

        for line in config_content.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            clean_lines.append(line)

        clean_config_content = "".join(clean_lines)
        config_data = json.loads(clean_config_content)

        self.validated_config = DataValidator.model_validate(config_data)
