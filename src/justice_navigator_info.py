from datetime import datetime
from colorama import init, Fore, Back, Style            # type: ignore

autoreset=True

def my_info() -> None:
    name = "DeAnna Hoskins, Roland Carlisle, Michael Washington, Miguel Pena"
    school = "Justice Through Code @ Columbia University -- Capstone Project"
    proj_name = "Justice Navigator - Journal Companion"
    separator = "=" * 64
    print(f"{Fore.WHITE}{separator}")
    print(f"\n{Fore.GREEN}{name}")
    proj_sep = "=" * 13
    proj_sep_end = "=" * 14
    print(f"{Fore.CYAN}{proj_sep}{proj_name}{proj_sep_end}")
    star = "*"
    print(f"{Fore.YELLOW}{star}{school}{star}{Style.RESET_ALL}")

my_info()

def show_date() -> None:
    now = datetime.now()
    readable = now.strftime("%B %d, %Y at %I:%M:%S %p")
    sep_16 = "=" * 16
    sep_64 = "=" * 64
    print(f"{Fore.WHITE}{sep_16}{readable}{sep_16}\n")
    print(f"{Fore.WHITE}{sep_64}{Style.RESET_ALL}")

show_date()
