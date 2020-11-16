#!/usr/bin/env python3
"""
Programme pour afficher des données avec datetime

Par Yanik Sweeney
"""

import datetime


def main() -> None:
    """Fonction principale"""
    now = datetime.datetime.now()
    print_elem("maintenant", now)
    print_elem("aujourd'hui", now.date())
    deltat = datetime.timedelta(1)
    print_elem("demain", now.date() + deltat)
    deltat = datetime.timedelta(-2)
    print_elem("avant-hier", now.date() + deltat)
    noel = "2020-12-25"
    noeldt = datetime.datetime.strptime(noel, "%Y-%m-%d")
    print_elem("noel", noeldt.date())
    noeldelta = noeldt - now
    print_elem("noel dans", f"{noeldelta.days} jours")


def print_elem(cle, valeur) -> None:
    """Print un ensemble cle: valeur"""
    print(f"{cle:>12}:", valeur)


if __name__ == '__main__':
    main()
