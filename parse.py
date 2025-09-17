from asyncio import Server
from tokens.parsable_tokens import UnparsedTokens
from tokens.lexable_tokens import *
from reports.reports import *
from reports.summary import *
from tokens._token import *
from error import *

# def map(tokens: list[Token]) -> Map:
#   MAP: [COL[], COL[]]

REPORT_TYPE_INDEX: int = 2
MACHINE_NAME: int = 6

def parse_status_report(unparsed: UnparsedTokens) -> StatusReport:
  machine_name: str = ""

  unparsed.get_token_at(MACHINE_NAME)
  machine_name += str(unparsed.token.value)

  report: StatusReport = StatusReport(machine_name)

  print(f"{BUFF}{INFO}[{unparsed.current_report + 1}]{RESET} {YELLOW}Parsing status report{RESET}: {machine_name}")

  return report


# TODO Not implemented at all and may need alot more processing
def parse_database_report(unparsed: UnparsedTokens) -> DatabaseReport:
  error("Cannot parse database report", "Not implemented", True)
  machine_name: str = ""

  unparsed.get_token_at(MACHINE_NAME)
  machine_name += str(unparsed.token.value)

  report: DatabaseReport = DatabaseReport(machine_name)

  print(f"{BUFF}{INFO}[{unparsed.current_report + 1}]{RESET} {YELLOW}Parsing database report{RESET}: {machine_name}")

  return report


# Will convert the tokens into a list of reports
def parse(unparsed: UnparsedTokens) -> Reports:
  status_reports: list[StatusReport] = []
  database_reports: list[DatabaseReport] = []

  print(f"{BUF}Initialized {BOLD}status{RESET} and {BOLD}server report{RESET} arrays")

  # Itterate through the reports
  while unparsed.current_report != unparsed.last_report:
    # First determine if it is a status or database report
    unparsed.get_token_at(REPORT_TYPE_INDEX)

    if unparsed.token.type != WORD:
      error(f"Expected either 'Status' or 'Database' report", "Please double check that every file within the target folder is a report")

    report_type: str = unparsed.token.value # type: ignore

    if report_type == "Status":
      status_reports.append(parse_status_report(unparsed))
    elif report_type == "Database":
      database_reports.append(parse_database_report(unparsed))
    else:
      error("Could not determine the type of report", f"Expected either 'Status' or 'Database' report type, however recieved: '{report_type}'")

    unparsed.next_report()
    pass

  return Reports(status_reports, database_reports)
