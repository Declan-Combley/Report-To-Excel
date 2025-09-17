from turtle import Terminator
from typing import NoReturn
from unittest.mock import DEFAULT
from colours import *

PREFIX: str = f"\n{BUF}{BAD}Error:{RESET} "
INDENTED_INFO_PREFIX: str = f"\n{BUFF}"

DEFAULT_ERROR: str = f"{PREFIX}Unexpected Error"
DEFAULT_INDENTED_INFO: str = "No further information"


def unspecified_error() -> NoReturn:
  print(DEFAULT_ERROR + DEFAULT_INDENTED_INFO)
  exit(1)

def error(error_header: str, indented_info: str, terminate: bool = False) -> None | NoReturn:
  print(PREFIX + error_header + INDENTED_INFO_PREFIX + indented_info)
  if terminate: exit(1)
