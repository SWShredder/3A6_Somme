#!/usr/bin/env python3
"""
Grep en python

Par Yanik Sweeney
"""

import re
import sys
import colorama
from colorama import Fore


def main() -> None:
    """Fonction principale"""
    colorama.init()
    check_usage()
    input_text = sys.stdin.readlines()
    regex_arg = sys.argv[1]
    compteur = 0
    for ligne in input_text:
        if re.search(regex_arg, ligne):
            print(ligne, end="")
            compteur += 1
    if compteur == 1:
        afficher_correspondances(f"{compteur} correspondance")
    elif compteur:
        afficher_correspondances(f"{compteur} correspondances")
    else:
        afficher_correspondances("aucune correspondance")


def check_usage() -> None:
    """Vérifie les arguments et retourne un message d'erreur au besoin"""
    arg_length = len(sys.argv) - 1
    if arg_length != 1:
        print(Fore.RED + "Le script s'attend à recevoir 1 argument,"
                         " mais vous en avez fourni", arg_length, file=sys.stderr)
        print(Fore.YELLOW + "USAGE: ./pygrep.py pattern" + Fore.WHITE, file=sys.stderr)
        sys.exit(1)


def afficher_correspondances(message: str) -> None:
    """Affiche la string de correspondances"""
    print(Fore.YELLOW + f"\n[ {message} ]" + Fore.WHITE, file=sys.stderr)


if __name__ == '__main__':
    main()
