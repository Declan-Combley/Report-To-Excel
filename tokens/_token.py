iota: int = 0
def enum(reset:bool = False) -> int: # Mimics Enums
    global iota
    if reset:
        iota = 0
    result: int = iota
    iota += 1
    return result

# Chose using enums instead of classes because I like to be able to debug using the printable tokens
# NOTE: The printable tokens and types must much up otherwise they will be indexed wrong,
#           and when you attempt to debug using the printable tokens all of them will be off
NUMBER = enum() # Float or Int
FLOAT = enum() #1.1
LETTER = enum() # a
WORD =  enum() # abc
SYMBOL = enum()
DOT = enum() # .
COMMA = enum() # ,
PAREN = enum() # ( or )
PERCENT = enum() # %
DATE = enum() # 01/01/2001
SPACE = enum()
NEWLINE = enum()
UNKNOWN = enum()
END = enum()
ERR = enum()

# Use this with the index of a type to get a printable version
#   E.g. print(PRINTABLE_TOKENS[NUMBER]) would return "NUMBER"
PRINTABLE_TOKENS: list[str] = ["NUMBER", "FLOAT", "LETTER", "WORD", "SYMBOL", "DOT", "COMMA", "PARENTHESIS", "PERCENT", "DATE", "SPACE", "NEWLINE", "UNKNOWN", "END", "ERR"]


class Token:
    type: int
    value: int | float | str

    def __init__(self, type: int, value: int | float | str) -> None:
        self.type = type
        self.value = value
