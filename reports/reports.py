from database import *
from tokens.lexable_tokens import *

class Disk:
  def __init__(self) -> None:
      self.mount_point: str = ""
      self.percent_free: float = 0.0

class Utilisation:
  def __init__(self) -> None:
      self.percent: float = 0.0
      self.physical_memory_low: bool = False
      self.virtual_memory_low: bool = False

class Memory:
  def __init__(self) -> None:
      self.availability: str = ""
      self.utilisation: Utilisation = Utilisation()
      self.disks: list[Disk] = []

class StatusReport:
  def __init__(self, name: str) -> None:
    self.name: str = name
    self.dbs: list[Database] = []
    self.memory: Memory = Memory()
    self.utilisation: Utilisation = Utilisation()

class DatabaseReport:
  def __init__(self, name: str) -> None:
    self.name: str = name


class Reports:
  def __init__(self, status_reports: list[StatusReport], database_reports: list[DatabaseReport]) -> None:
    self.status_reports: list[StatusReport] = status_reports
    self.database_reports: list[DatabaseReport] = database_reports
    pass


  # TODO
  def summarise(self) -> None:
    pass