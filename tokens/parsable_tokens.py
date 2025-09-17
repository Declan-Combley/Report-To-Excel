from tokens._token import *
from error import *

class UnparsedTokens:
  index: int = 0
  next_index: int = 0

  current_report: int = 0


  def __init__(self, unparsed_tokens: list[list[Token]]) -> None:
    self.report_tokens: list[list[Token]] = unparsed_tokens

    self.tokens: list[Token] = self.report_tokens[0]
    self.token: Token = self.tokens[0]

    self.no_of_tokens: int = len(self.tokens)
    self.last_report: int = len(self.report_tokens)


  # Move onto the next set of reports tokens
  def next_report(self) -> None:
    # Ensure that we aren't already on the last set of tokens
    if self.current_report == self.last_report - 1:
      self.current_report = self.last_report
      return

    # Move onto the next report
    self.current_report += 1
    self.tokens = self.report_tokens[self.current_report]
    self.no_of_tokens = len(self.tokens)

    # Reset Indexes
    self.index = 0
    self.next_index = 0


  # Will get a value and
  def get_token_at(self, target_index: int) -> None:
    if target_index >= self.no_of_tokens - 1:
      error(f"Could not get value as index is out of bounds: {target_index}", f"Number of tokens: {self.no_of_tokens}")

    self.next_index = target_index
    self.token = self.tokens[self.next_index]


  def next_token(self) -> None:
    if self.current_report != self.last_report - 1:
      return

    self.index = self.next_index
    # self.current_report += 1
    # self.tokens = list[self.current_report]

  # def gather(self, end_term: str, type: int):
  #   pass

  def gather(self, term: str | int, type) -> Token:
    return Token(ERR, "")

  # Will find the index of a term
  def search_for(self, term: str | int):
    pass