#!/usr/bin/env python3

"""
Programme pour ouvrir océans.txt

Par Yanik Sweeney
"""

import sys
import colorama
from colorama import Fore, Style
colorama.init()


def main() -> None:
    """Fonction principale"""
    fichier = "océans.txt"
    try:
        with open(fichier) as f:
            text = f.read()
            print(Style.BRIGHT + Fore.CYAN + text)
    except FileNotFoundError:
        erreur(f"Le fichier '{fichier}' n'existe pas.")


def erreur(msg: str) -> None:
    """Affiche un message d'erreur, puis termine le script"""
    print(Fore.RED + msg, file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    main()
