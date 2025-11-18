
from colorama import Fore, Back, Style
from random import choice

logo = """

███╗░░░███╗███████╗████████╗░█████╗░  ░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░
████╗░████║██╔════╝╚══██╔══╝██╔══██╗  ██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
██╔████╔██║█████╗░░░░░██║░░░███████║  ╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║  ░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║  ██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝ """

urls = [
    "GitHub - https://github.com/ziddi-shop",
    "Instagram - https://instagram.com/yknowxziddi",
    "Telegram - https://t.me/meta_server",
    "Telegram - https://t.me/nobi_shops",
    "InstaReporter Tool - https://github.com/ziddi-shop/Instagram-Report-Tool",
    "Gmail - mailto:shehzadakingziddi@gmail.com"
    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Producer: ZIDDI"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> Follow me On Instagram @yknowxziddi.")
    print ("\n", "-> Meta Server:\n    " + choice(urls))
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
