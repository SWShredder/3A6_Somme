#!/usr/bin/env python3

"""
Programme pour afficher les arguments

Par Yanik Sweeney
"""

import pprint
import sys


def main() -> None:
    """Fonction principale"""
    pprint.pprint(sys.argv, width=40)
    print()
    print(f"Il y a {len(sys.argv) - 1} arguments")
    for i, arg in enumerate(sys.argv):
        print(f" - arg {i}: {arg}")


if __name__ == '__main__':
    main()
