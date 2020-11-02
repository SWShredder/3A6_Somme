#!/usr/bin/env python3
"""
Echo en python

Par Yanik Sweeney
"""

import os
import sys


def main() -> None:
    """Fonction principale"""

    if sys.stdin.isatty():
        print("Aucune redirection d'entrée à traiter")
        return

    lignes = sys.stdin.readlines()

    if not lignes:
        return

    for ligne in lignes[:-1]:
        print(ligne, end="")
        print(*sys.argv[1:], sep="\n")

    print(lignes[-1], end="")


if __name__ == '__main__':
    main()