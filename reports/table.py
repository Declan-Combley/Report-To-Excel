from typing import Dict
from descriptions import *

class Values:
  value: list[Descriptor | int | float | str ]

  def __init__(self, no: int = 1) -> None:
      # The index will be where the beginning of the token should be found
      self.index = no - 1

class Table:
  def __init__(self, table: Dict, static: bool = False):
    self.table = table
    self.static = static

  # TODO
  def get_value(self, key: str):
    pass

# TABLES THAT WILL BE USED IN REPORTS
class DiskSpace(Table):
  info: Dict[str, Values] = {
    "Mount Point" : Values(),
    "Available Size GB" : Values(),
    "Space Free %" : Values()
  }

  def __init__(self) -> None:
    super().__init__(self.info)


class MemoryAvailability(Table):
  info: Dict[str, Values] = {
    "System Memory State" : Values(),
  }

  def __init__(self) -> None:
    super().__init__(self.info)


class LogFileInformation(Table):
  info: Dict[str, Values] = {
    "DB Compatability Level" : Values(),
  }

  def __init__(self) -> None:
    super().__init__(self.info)


class DiskIoStatus(Table):
  info: Dict[str, Values] = {
    "Database Name" : Values(),
    "File Name" : Values(),
    "Avg IO Stall ms" : Values(),
    "IO Status" : Values(),
  }

  def __init__(self) -> None:
    super().__init__(self.info)