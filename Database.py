from descriptions import *

class DBFile:
  def __init__(self,name: str) -> None:
    self.name: str = name

    self.read_latency: float = 0.0
    self.write_latency: float = 0.0
    self.avg_disk_latency: float = 0.0

    self.avg_io_stall: float = 0.0
    self.avg_status: Descriptor = Default()
    self.io_latency_status: Descriptor = Default()


class Database:
  def __init__(self, name: str) -> None:
    self.name: str = name
    self.files: list[DBFile] = []