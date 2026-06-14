"""try / except / else / finally Control Flow

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from pathlib import Path

_load_attempts = 0

def safe_load_dataset(path: str | Path) -> list[str]:
    """Read lines from `path`. Return [] if the file is missing/unreadable.
    Always increment the module-level _load_attempts counter, on success OR failure.
    Parse (split into lines) ONLY when the read succeeded.
    """
    global _load_attempts
    # TODO: try -> read; except OSError -> return []; else -> split lines;
    #       finally -> bump _load_attempts
    raise NotImplementedError
"""

# Your code here.
