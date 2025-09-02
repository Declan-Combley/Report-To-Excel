from tkinter import CURRENT
import PyPDF2 # pyright: ignore[reportMissingImports]
from typing import BinaryIO # type: ignore
from Descriptions import *
from StatusReport import *
from ServerReport import *
from Summary import *
from colours import *


enum: int = 0
def iota(reset:bool = False) -> int: # Mimics Enums
    global enum
    if reset:
        enum = 0
    result: int = enum
    enum += 1
    return result


NUMBER = iota() # 1
LETTER = iota() # a
WORD =  iota() # abc
SYMBOL = iota()
DOT = iota() # .
COMMA = iota() # ,
PAREN = iota() # ( or )
PERCENT = iota() # %
DATE = iota() # 01/01/2001
SPACE = iota()
NEWLINE = iota()
UNKNOWN = iota()
END = iota()
ERR = iota()

# PRINTABLE_TOKENS: list[str] = ["NUMBER", "LETTER", "WORD", "SYMBOL", "DOT", "COMMA", "PERCENT", "DATE", "SPACE", "NEWLINE", "UNKNOWN", "END", "ERR"] Without Paren
PRINTABLE_TOKENS: list[str] = ["NUMBER", "LETTER", "WORD", "SYMBOL", "DOT", "COMMA", "PARENTHESIS", "PERCENT", "DATE", "SPACE", "NEWLINE", "UNKNOWN", "END", "ERR"]


class Token:
    type: int
    value: int | float | str

    def __init__(self, type: int, value: int | float | str) -> None:
        self.type = type
        self.value = value


class UnlexedTokens:
    tokens: list[Token]

    current: Token
    next: Token

    amount: int
    index: int = 1

    def __init__(self, tmp_tokens: list[Token]) -> None:
        self.tokens = tmp_tokens # Should stay unchanged after initialization

        self.amount = len(tmp_tokens)
        tmp_tokens.append(Token(END, ""))

        self.current = tmp_tokens[0]
        self.next = tmp_tokens[1]

        print(f"{BUFF}Appended {BOLD}END{RESET} token.")

    # Should be the only way to itterate through the tokens
    def next_token(self) -> None:
        if self.current.type == END or self.next.type == END:
            self.index += 1
            print(f"{BUFFF}{RED}Hit Last Token.{RESET}")
            return

        self.current = self.next
        self.index += 1

        self.next = self.tokens[self.index]

    # Deterimines if the current token can be skipped
    def current_token_is_skipable(self) -> bool:
        type: int = self.current.type
        if type == SPACE or type == COMMA or type == NEWLINE or type == PAREN:
            return True
        return False

    # Deterimines if the current token can be skipped
    def next_token_is_skipable(self) -> bool:
        type: int = self.next.type
        if type == SPACE or type == COMMA or type == NEWLINE or type == PAREN:
            return True
        return False


class LexedTokens:
    def __init__(self) -> None:
        self.tokens: list[Token] = []

    def add_current_token_from(self, unlexed_tokens: UnlexedTokens) -> None:
        if unlexed_tokens.current.type == END:
            return
        self.tokens.append(unlexed_tokens.current)
        unlexed_tokens.next_token()

    def add_new_token(self, token: Token, unlexed_tokens: UnlexedTokens) -> None:
        self.tokens.append(token)
        unlexed_tokens.next_token()


def character_to_token(char:str) -> Token:
    try:
        if char.isdigit():
            return Token(NUMBER, char)
        if char.isalpha():
            return Token(LETTER, char)
        if char == ':' or char == '_' or char == '-' or char == '/' or char == '\'':
            return Token(SYMBOL, char)
        if char == '(' or char == ')':
            return Token(PAREN, char)
        if char == '.':
            return Token(DOT, char)
        if char == ',':
            return Token(COMMA, char)
        if char == '%':
            return Token(PERCENT, char)
        if char == ' ' or char == '\t':
            return Token(SPACE, char)
        if char == '\n' or char == '\r':
            return Token(NEWLINE, "\\n")
        else:
            return Token(UNKNOWN, char)
    except IndexError:
        return Token(ERR, char)


# TODO: def tokenize_number(tmp_tokens: list[Token], tokens: list[Token], index: int) -> list[Token]:

# Will concatonate every token up until a space, newline, or End token
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

    #         print(f"Character '{char if token.type != NEWLINE else "\\n"}' converted to {BOLD}{PRINTABLE_TOKENS[token.type]}{RESET} with value '{token.value}'")

    unlexed_tokens: UnlexedTokens = UnlexedTokens(tmp_tokens) # Unlexed tokens should remain unchanged
    lexed_tokens: LexedTokens = LexedTokens()

    # while unlexed_tokens.index <= unlexed_tokens.amount:
    while unlexed_tokens.next.type != END:
        # print(f"{BUFFF}{BOLD}Current Index:{RESET} {unlexed_tokens.index}")
        # print(f"{BUFFF}{BOLD}Current Token: {RESET} {unlexed_tokens.current.value}")

        if unlexed_tokens.current_token_is_skipable():
            print(f"{BUFFF}Skipping {BOLD}{PRINTABLE_TOKENS[unlexed_tokens.current.type]}{RESET} token at index {unlexed_tokens.index}")
            unlexed_tokens.next_token()
            continue

        if unlexed_tokens.current.type == NUMBER:
            pass
            # tokenize_number(tmp_tokens, tokens, index)
        elif unlexed_tokens.current.type == LETTER:
            if unlexed_tokens.next.type == LETTER or unlexed_tokens.next.type == SYMBOL: # <-- Covers |a | a,| a\n|
                tokenize_word(unlexed_tokens, lexed_tokens)
                continue

            lexed_tokens.add_current_token_from(unlexed_tokens)
        unlexed_tokens.next_token()

    print(f"\n{BUFF}Amount of tokens {BOLD}prior{RESET} to lexing -> {unlexed_tokens.amount}")
    print(f"{BUFF}Amount After -> {INFO}{len(lexed_tokens.tokens)}{INFO}")
    print(f"{GOOD}\nTokenization complete.\n")
    return lexed_tokens.tokens


def parse(tokens: list[Token]) -> StatusReport | ServerReport | None:
    return None