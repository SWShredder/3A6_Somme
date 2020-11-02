#!/usr/bin/env python3
"""
Eval

Par Yanik Sweeney
"""

import getpass
import sys
import colorama
import os
import math
from math import *
from colorama import Fore, Style
colorama.init()


def main() -> None:
    """Fonction principale"""
    verifier_usage()
    user = getpass.getuser()
    try:
        result = eval("".join(sys.argv[1:]))
        print(Fore.CYAN + Style.BRIGHT + f"Selon {user} : {result}")
    except Exception as ex:
        erreur(str(ex))


def verifier_usage() -> None:
    """
    Vérifie l'usage du programme et en cas d'erreur,
    affiche un message d'erreur et un usage, puis termine le script
    """
    nbargs = len(sys.argv) - 1
    if nbargs < 1:
        nom_script = os.path.join('.', os.path.basename(sys.argv[0]))
        erreur(
            f"Le script s'attend à recevoir 1 argument, mais vous en avez fourni {nbargs}\n" +
            Fore.YELLOW + f"USAGE: {nom_script} StringToEval"
        )


def erreur(msg: str) -> None:
    """Affiche un message d'erreur, puis termine le script"""
    print(Fore.RED + msg, file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    main()
