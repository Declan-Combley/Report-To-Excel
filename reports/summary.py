from descriptions import *
from reports.reports import *

ERROR: str = "ERROR"

class Summary:
    def __init__(self, reports: Reports) -> None:
        self.reports = reports
        self.backups: list[Descriptor] = []
        self.DiscSpace: list[Descriptor] = []
        self.DiscIO: list[Descriptor] = []
        self.ReadLatency: list[Descriptor] = []
        self.WriteLatency: list[Descriptor] = []
        self.IndexFragmentation: list[Descriptor] = []
        self.MemoryUtilisation: list[Descriptor] = []
        self.MemoryAvailability: list[Descriptor] = []

    def convert_to_excel(self) -> None:
        pass

# class Text:
#     def __init__(self, text: str, index: int) -> None:
#         self.text: str = text
#         self.index: int = index
#         self.prev_index: int = index
#         self.found: bool = True

#     def search(self, term: str) -> None:
#         self.prev_index = self.index
#         self.index = self.text.find(term, self.index)

#         if self.index == -1:
#             self.index = self.prev_index
#             self.found = False
#             return

#         self.index += len(term) + 1


#     def gather(self, term: str, ending_term: str) -> str: # Searches for term, then gathers everything until ending_term
#         self.search(term)
#         if not self.found:
#             return ERROR

#         start_index: int = self.index
#         self.search(ending_term)

#         if not self.found:
#             return ERROR

#         value: str = ""
#         while start_index < self.index:
#             char = self.text[start_index]
#             if char == "\n":
#                 break

#             value += char
#             start_index += 1
#         self.index += 1

#         return value.strip()
