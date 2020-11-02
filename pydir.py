#!/usr/bin/env python3
"""
Script pour afficher des éléments du dossier

Par Yanik Sweeney
"""

import glob
import sys


def main() -> None:
    """Fonction principale"""
    if len(sys.argv) == 1:
        s = glob.glob("*.py")
        s.sort()
        print(*s, sep="\n")

    else:
        s = []
        for element in sys.argv[1:]:
            s.append(glob.glob(element))
        s.sort()
        for element in s:
            print(*element, sep="\n")


if __name__ == '__main__':
    main()