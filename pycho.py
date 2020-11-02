#!/usr/bin/env python3
"""
Echo en python

Par Yanik Sweeney
"""

import os
import sys


def main() -> None:
    """Fonction principale"""
    print(*sys.argv[1:])


if __name__ == '__main__':
    main()
