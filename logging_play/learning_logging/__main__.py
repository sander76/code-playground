import logging
from pathlib import Path

import typer
from learning_logging import a_package
from learning_logging.another_package import module_inside_package
from learning_logging.logging_config import load_toml_logger, load_yaml

_LOGGER = logging.getLogger(__name__)

app=typer.Typer()

@app.command()
def load_toml_config(filename:Path):
    print(f"using config file {filename}")
    if filename.suffix in (".toml",".tml"):
        print("loading toml file")
        load_toml_logger(filename)
    elif filename.suffix in (".yml",".yaml"):
        print("loading yaml file")
        load_yaml(filename)
    else:
        raise FileNotFoundError("no proper config file found")

    _LOGGER.info("This is a test")
    a_package.run_a_function()

    module_inside_package.execute_this_function()

app()