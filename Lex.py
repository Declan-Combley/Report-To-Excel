import PyPDF2 # pyright: ignore[reportMissingImports]
from typing import BinaryIO # type: ignore
from colours import *
from tokens.lexable_tokens import *


# Will return the remaining digits of a number that has had everything before the elipses stripped
# NOTE: Will only be used within the tokenize_number function
def tokenize_float(unlexed_tokens: UnlexedTokens, number: str) -> str:
    print(f" ---> float", end="")
    unlexed_tokens.next_token()

    while unlexed_tokens.next.type == NUMBER:
        number += str(unlexed_tokens.current.value)
        unlexed_tokens.next_token()

    number += str(unlexed_tokens.current.value)

    return number


# Will tokenize numbers and floats
def tokenize_number(unlexed_tokens: UnlexedTokens, lexed_tokens: LexedTokens) -> None:
    print(f"{BUFFF}Encountered a number {INFO}{unlexed_tokens.current.value}...{RESET}", end="")
    number: str = ""

    # Will add the digits until there aren't anymore
    while unlexed_tokens.next.type == NUMBER:
        number += str(unlexed_tokens.current.value)
        unlexed_tokens.next_token()

    number += str(unlexed_tokens.current.value)

    # Will check if there is an elipsies that would indicate that the number is actually a float
    if unlexed_tokens.next.type == DOT:
        number = tokenize_float(unlexed_tokens, number) # Will get the remaining characters of the float and save it as such
        lexed_tokens.add_new_token(Token(NUMBER, float(number)), unlexed_tokens)
    else: # If not it will save the token as an integer
        lexed_tokens.add_new_token(Token(NUMBER, int(number)), unlexed_tokens)
        print(f" ---> int ", end="")

    print(f" ---> {BOLD}{number}{RESET}")


# Will concatonate every token up until a space, newline, or End token
# NOTE: Including numbers and symbols
def tokenize_word(unlexed_tokens: UnlexedTokens, lexed_tokens: LexedTokens) -> None:
    print(f"{BUFFF}Encountered the start of a word {INFO}{unlexed_tokens.current.value}{unlexed_tokens.next.value}...{RESET}", end="")
    word: str = ''

    while unlexed_tokens.next_token_is_skipable() == False:
        try:
            word += str(unlexed_tokens.current.value)
            unlexed_tokens.next_token()
        except ValueError:
            exit(1)

    word += str(unlexed_tokens.current.value)
    unlexed_tokens.next_token()

    lexed_tokens.add_new_token(Token(WORD, word), unlexed_tokens)
    print(f" ---> {BOLD}{word}{BOLD}")


# This will convert all of the PDF contents into computer readable tokens
def tokenize(PDF: BinaryIO) -> list[Token]:
    tmp_tokens: list[Token] = []

    print(f"{BUF}{YELLOW}Starting tokenization...")

    # Read PDF, extract characters and convert to initial tokens
    reader = PyPDF2.PdfReader(PDF)
    for page in reader.pages:
        text: str = page.extract_text()
        for char in text:
            token: Token = character_to_token(char)
            tmp_tokens.append(token)


    unlexed_tokens: UnlexedTokens = UnlexedTokens(tmp_tokens)
    lexed_tokens: LexedTokens = LexedTokens()

    # Itterate through all of the unlexed tokens
    while unlexed_tokens.next.type != END:
        # We can skip these becuase we now they aren't useful
        # (They would have been included as part of a previous float or word)
        if unlexed_tokens.current_token_is_skipable():
            print(f"{BUFFF}Skipping {BOLD}{PRINTABLE_TOKENS[unlexed_tokens.current.type]}{RESET} token at index {unlexed_tokens.index}")
            unlexed_tokens.next_token()
            continue

        # <--------- Covers integers and floats
        if unlexed_tokens.current.type == NUMBER:
            tokenize_number(unlexed_tokens, lexed_tokens)
            continue

        # <--------- Covers Words
        # NOTE: Words can include numbers and symbols E.g. "Computer/123"
        if unlexed_tokens.current.type == LETTER:
            if unlexed_tokens.next.type == LETTER or unlexed_tokens.next.type == SYMBOL: # <-- Covers singular letters
                tokenize_word(unlexed_tokens, lexed_tokens)
                continue

        # Accounts for all singular tokens as they will not have fallen under any of the other previous cases
        lexed_tokens.add_current_token_from(unlexed_tokens) # Inherently moves onto the next token and continues the loop


    print(f"{BUFFF}{RED}Hit Last Token.{RESET}")
    print(f"\n{BUFF}Amount of tokens {BOLD}prior{RESET} to lexing -> {unlexed_tokens.amount}")
    print(f"{BUFF}Amount After -> {INFO}{len(lexed_tokens.tokens)}{INFO}")
    print(f"{GOOD}\nTokenization complete.\n")

    return lexed_tokens.tokens