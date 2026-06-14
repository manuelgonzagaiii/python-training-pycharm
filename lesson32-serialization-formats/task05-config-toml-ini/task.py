"""Configuration: tomllib & configparser

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import tomllib
import configparser
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Settings:
    currency: str
    page_size: int

def load_toml(path) -> dict:
    with open(path, 'rb') as f:   # binary!
        return tomllib.load(f)

def load_ini(text: str) -> configparser.ConfigParser:
    cp = configparser.ConfigParser()
    cp.read_string(text)
    return cp

"""

# Your code here.
