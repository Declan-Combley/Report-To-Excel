from reports.reports import *
from reports.summary import *
from tokens.lexable_tokens import *
from tokens._token import *
from tokens.parsable_tokens import UnparsedTokens

# def map(tokens: list[Token]) -> Map:
#   MAP: [COL[], COL[]]

def parse_status_report(tokens: list[Token]) -> StatusReport:
  machine_name: str = ""
  report: StatusReport = StatusReport(machine_name)

  return report


def parse(unparsed: UnparsedTokens) -> Reports:
  status_reports: list[StatusReport] = []
  server_reports: list[DatabaseReport] = []

  print(f"{BUF}Initialized {BOLD}status{RESET} and {BOLD}server report{RESET} arrays")

  print()
  # for report in tokens_list:
  #   pass
    # for token in report:
    #   # First determine if it is a status or database report
    #   print(token.value)

  return Reports(status_reports, server_reports)
