# Configuration: tomllib & configparser

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.5 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Read app.toml settings with tomllib (note: read-only, must open in binary mode)
- Parse legacy INI logging config with configparser including typed getters
- Understand TOML's richer type system vs INI's string-only values
- Merge defaults with overrides into a settings object

## Python features introduced
`tomllib.load (binary mode)`, `tomllib.loads`, `TOML tables and types`, `configparser.ConfigParser`, `read_string / sections / get / getint / getboolean`, `interpolation (BasicInterpolation)`, `DEFAULT section`, `writing INI with config.write`

## MiniERP increment
Adds minierp/config.py: load_config(layout) reading config/app.toml (db path, currency, page size) and config/logging.ini, returning a typed Settings dataclass that the service/CLI layers consume - runtime config is now externalized.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import tomllib
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

- **Test focus:** A TOML string parses into nested tables with correct types (int/str/bool); tomllib raises if opened in text mode (concept tested via loads); configparser getint/getboolean coerce values; DEFAULT-section interpolation resolves.

</div>
