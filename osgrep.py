#!/usr/bin/env python3
"""
Grep en python utilisant les fonctions systèmes des OS linux ou windows

Par Yanik Sweeney
"""

import sys
import os
import shlex


def main() -> None:
    """Fonction principale"""
    args_list = []
    if os.name == "nt":
        for arg in sys.argv[1:]:
            a = arg.replace("\\", "\\\\")
            a = arg.replace('\"', '\\\"')
            args_list.append(f'"{a}"')
        args = ' '.join(args_list)
    else:
        args = shlex.join(sys.argv[1:])

    commande = "egrep " + args if os.name != "nt" else "findstr " + args
    exitcode = os.system(commande)
    if exitcode:
        print("La commande exécutée était:", commande, file=sys.stderr)
    sys.exit(exitcode)


if __name__ == '__main__':
    main()
