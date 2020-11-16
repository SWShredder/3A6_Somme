#!/usr/bin/env python3
"""
Grep en python

Par Yanik Sweeney
"""

import re
import sys


def main() -> None:
    """Fonction principale"""
    input_text = ''.join(sys.stdin.readlines())
    regex_arg = sys.argv[1]
    regex_result = re.search(regex_arg, input_text)
    print(regex_result)


if __name__ == '__main__':
    main()
