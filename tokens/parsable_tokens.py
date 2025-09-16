from tokens._token import *

class UnparsedTokens:
  index: int = 0
  next_index: int = 0

  current_report: int = 0

  def __init__(self, tokens: list[list[Token]]) -> None:
    self.lists: list[list[Token]] = tokens
    self.tokens = tokens[0]

    self.no_of_lists = len(tokens)

  def next_tokens(self) -> None:
    if self.current_report == self.no_of_lists - 1:
      return

    self.current_report += 1
    self.tokens = list[self.current_report]


  def gather(self, type: int):
    pass

  def search_for(self, term: str | int):
    pass