from typing import Any

from . import detect, logger, session, source, temp
from .__info__ import __author__, __doc__, __license__, __version__
from ._dill import (
    CONTENTS_FMODE,
    DEFAULT_PROTOCOL,
    FILE_FMODE,
    HANDLE_FMODE,
    HIGHEST_PROTOCOL,
    PickleError,
    Pickler,
    PickleWarning,
    PicklingError,
    PicklingWarning,
    Unpickler,
    UnpicklingError,
    UnpicklingWarning,
    check,
    copy,
    dump,
    dumps,
    load,
    loads,
    pickle,
    pickles,
    register,
)
from .session import dump_module, dump_session, load_module, load_module_asdict, load_session
from .settings import settings

__all__ = [
    "__author__",
    "__doc__",
    "__license__",
    "__version__",
    "CONTENTS_FMODE",
    "DEFAULT_PROTOCOL",
    "FILE_FMODE",
    "HANDLE_FMODE",
    "HIGHEST_PROTOCOL",
    "PickleError",
    "PickleWarning",
    "Pickler",
    "PicklingError",
    "PicklingWarning",
    "Unpickler",
    "UnpicklingError",
    "UnpicklingWarning",
    "check",
    "copy",
    "dump",
    "dumps",
    "load",
    "loads",
    "pickle",
    "pickles",
    "register",
    "dump_module",
    "dump_session",
    "load_module",
    "load_module_asdict",
    "load_session",
    "detect",
    "logger",
    "session",
    "source",
    "temp",
    "settings",
]

objects: dict[str, Any]

def load_types(pickleable: bool = ..., unpickleable: bool = ...) -> None: ...
def extend(use_dill: bool = ...) -> None: ...
def license() -> None: ...
def citation() -> None: ...
