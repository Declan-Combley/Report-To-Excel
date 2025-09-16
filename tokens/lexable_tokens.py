from colours import *
from ._token import *

class UnlexedTokens:
    tokens: list[Token]

    current: Token
    next: Token

    amount: int
    index: int = 1

    def __init__(self, tmp_tokens: list[Token]) -> None:
        self.tokens = tmp_tokens # Tmp tokens should stay unchanged after initialization

        self.amount = len(tmp_tokens)

        tmp_tokens.append(Token(SPACE, " ")) # Spacer
        tmp_tokens.append(Token(END, ""))

        self.current = tmp_tokens[0]
        self.next = tmp_tokens[1]

        print(f"{BUFF}Appended {BOLD}END{RESET} token.")

    # Should be the only way to itterate through the tokens
    def next_token(self) -> None:
        if self.current.type == END or self.next.type == END:
            self.index += 1
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
    if char.isdigit():
        return Token(NUMBER, int(char))
    if char.isalpha():
        return Token(LETTER, char)
    if char == ':' or char == '_' or char == '-' or char == '/' or char == '\\' or char == '$':
        return Token(SYMBOL, char)
    if char == '(' or char == ')' or char == '[' or char == ']' or char == '{' or char == '}':
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


def print_token(token: Token) -> None:
    print(f"{BOLD}{PRINTABLE_TOKENS[token.type]}{RESET} --> {token.value}")


def print_problem_tokens(tokens: list[Token]) -> None:
    no_problem_tokens_exist: bool = True
    for token in tokens:
        if token.type == UNKNOWN or token.type == ERR:
            print(f"{BUFF}{PRINTABLE_TOKENS[token.type]} --> {BAD}{token.value}")
            no_problem_tokens_exist = False

    if no_problem_tokens_exist:
        print(f"{BUFF}{GOOD}None.")
    print()