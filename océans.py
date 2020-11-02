#!/usr/bin/env python3
"""
Programme pour créer un fichier oceans.txt

Par Yanik Sweeney
"""


def main() -> None:
    """Fonction principale"""
    oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

    with open("océans.txt", "w") as f:
        for ocean in oceans:
            print(ocean, file=f)

    with open("océans.txt", "a") as f:
        print(23 * "=", file=f)
        print("Les 5 océans, par Yanik Sweeney", file=f)


if __name__ == '__main__':
    main()
