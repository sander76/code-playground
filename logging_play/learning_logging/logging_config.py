from logging.config import dictConfig

from pathlib import Path
import toml
import yaml


def load_toml_logger(logfile: Path):
    with open(logfile) as fl:
        _dict = toml.load(fl)

    load_config(_dict)

def load_yaml(logfile:Path):
    with open(logfile) as fl:
        config = yaml.safe_load(fl.read())

    load_config(config)

def load_config(config:dict):
    _config = dictConfig(config)
