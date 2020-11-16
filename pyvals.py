#!/usr/bin/env python3
"""
Programme pour évaluer une expression Python
(version simplifiée)

Par Yanik Sweeney
"""

import colorama
from colorama import Fore
import math
from math import *
import sys


GLOBALS = {
    "__builtins__": {},
    **math.__dict__,
    "abs": abs,
    "min": min,
    "max": max,
    "sum": sum,
}
LOCALS = {}


def main() -> None:
    """Fonction principale"""
    arg_list = []
    for arg in sys.argv[1:]:
        arg_list.append(arg.replace("__", ""))
    try:
        print(Fore.CYAN + "Selon Yanik Sweeney", Fore.RESET,
              eval(' '.join(arg_list) or "None", GLOBALS, LOCALS))

    except Exception as ex:
        print(Fore.RED, ex, file=sys.stderr, sep="")
        sys.exit(1)


if __name__ == '__main__':
    colorama.init()
    main()
