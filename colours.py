from colorama import Fore, Style, init

init(autoreset=True)

BOLD = Style.BRIGHT
RESET = Style.RESET_ALL

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED

GOOD = GREEN + BOLD
BAD = RED + BOLD
INFO = YELLOW + BOLD

BUF: str = "  "
BUFF: str = BUF + BUF
BUFFF: str = BUF + BUFF