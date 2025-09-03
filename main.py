from reports.reports import *
from reports.summary import *
from parse import *
from lex import *
import os, glob
import sys


def open_file(file_path: str) -> BinaryIO:
    try:
        PDF: BinaryIO = open(file_path, 'rb')
        return PDF
    except FileNotFoundError:
        print(f"{BUF}{BAD}Error:{RESET} Could not find {INFO}{file_path}{RESET}, please ensure that it is not corrupted, and still exists.")
    except PermissionError:
        print(f"{BUF}{BAD}Error: {RESET} You do not have permission to access this file.")
    except Exception as error:
        print(f"{BUF}{RED}An unexpected error occurred: {error}")
    exit(1)


def main() -> int:
    tokens: list[list[Token]] = []
    no_of_arguments: int = len(sys.argv)

    if no_of_arguments >= 2: # Ensure there are input files
        folder_name: str = sys.argv[1]

        folder = glob.glob(os.path.join(folder_name, "*.pdf"))

        if len(folder) == 0:
            print(f"{BUF}{BAD}Error:{RESET} Could not find any files in {INFO}{folder_name}{RESET}")
            print(f"{BUFF}Please ensure that it exists and that there are SQL HealthCheck {INFO}PDFs{RESET} in it.")
            exit(1)

        # Itterate through and tokenize all of the files and store them in a tokens array
        file_no: int = 0
        for PDF in folder:
            with open_file(PDF) as PDF:
                print(f"{INFO}[{file_no}]{RESET} {YELLOW}Processing file:{RESET} {PDF}")

                lexed_tokens: list[Token]  = tokenize(PDF)
                tokens.append(lexed_tokens)
                file_no += 1
    else: # If there aren't any input files error out
        print(f"{BAD}Error{RESET}: No folder path provided, please {BOLD}add a file{RESET} by copying its route as such.")
        print(f"{BUF}{INFO}Example{RESET}: python main.py {GREEN}./Folder")
        exit(1)

    list_of_all_tokens: list[Token] = [token for token_list in tokens for token in token_list]

    print(f"{BOLD}Files processed:{RESET} {len(tokens)}")
    print(f"{BOLD}Tokens extracted:{RESET} {len(list_of_all_tokens)}")

    print(f"\n{BUF}{INFO}Problematic Tokens{RESET}: ")
    print_problem_tokens(list_of_all_tokens)


    print(f"{YELLOW}Beggining parsing process...")
    reports: Reports = parse(tokens) # In progress

    summary: Summary = Summary(reports) # Create output using the reports
    summary.reports.summarise() # TODO
    summary.convert_to_excel() # TODO

    return (0)


if __name__ == "__main__":
    exit(main())
else:
    exit(1)