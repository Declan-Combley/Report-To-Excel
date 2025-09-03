from typing import BinaryIO # type: ignore
from descriptions import *
from statusReport import *
from serverReport import *
from summary import *
from lex import *
from colours import *
import sys


def print_tokens(tokens: list[Token]) -> None:
    for token in tokens:
        if token.type == UNKNOWN:
            print(f"{BUF}{BAD}UNKNOWN{RESET} | {INFO}{token.value}")
        else:
            print(f"{BUF}{BOLD}{PRINTABLE_TOKENS[token.type]}{RESET} ---> {token.value}")


def open_file(file_path: str) -> BinaryIO:
    try:
        PDF: BinaryIO = open(file_path, 'rb')
        return PDF
    except FileNotFoundError:
        print(f"{BAD}Error:{RESET} Could not find {INFO}{file_path}{RESET}, please double check where that file may be stored.")
    except PermissionError:
        print(f"{BAD}Error: {RESET} You do not have permission to access this file.")
    except Exception as error:
        print(f"{RED}An unexpected error occurred: {error}")
    exit(1)


def main() -> int:
    input_files_no: int = len(sys.argv) - 1
    unparsed_tokens: list[list[Token]] = []

    if input_files_no != 0:
        files_names: list[str] = sys.argv[1:]

        index: int = 1
        for PDF_location in files_names:
            with open_file(PDF_location) as PDF:
                print(f"{INFO}[{index}]{RESET} {YELLOW}Processing file:{RESET} {PDF_location}")

                lexed_tokens: list[Token]  = tokenize(PDF)
                unparsed_tokens.append(lexed_tokens)
                index += 1
    else:
        print(f"{BAD}Error{RESET}: No file path provided, please {BOLD}add a file{RESET} by copying its route as such.")
        print(f"{BUF}{INFO}Example{RESET}: python main.py {GREEN}./Examples/test.pdf")
        exit(1)

    print(f"{INFO}Tokens:{RESET}")
    for token in unparsed_tokens:
        print_tokens(token)

    print("")

    print(f"{BOLD}Files processed:{RESET} {len(unparsed_tokens)}")
    print(f"{BOLD}Tokens gleamed:{RESET} {sum(len(tokens) for tokens in unparsed_tokens)}\n")

    return (0)


if __name__ == "__main__":
    exit(main())
else:
    exit(1)