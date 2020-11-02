#!/usr/bin/env python3
"""
Programme pour afficher des données avec datetime

Par Yanik Sweeney
"""

import datetime


def main() -> None:
    """Fonction principale"""
    now = datetime.datetime.now()
    printElement("maintenant", now)
    printElement("aujourd'hui", now.date())
    deltat = datetime.timedelta(1)
    printElement("demain", now.date() + deltat)
    deltat = datetime.timedelta(-2)
    printElement("avant-hier", now.date() + deltat)
    noel = "2020-12-25"
    noeldt = datetime.datetime.strptime(noel, "%Y-%m-%d")
    printElement("noel", noeldt.date())
    noeldelta = noeldt - now
    printElement("noel dans", f"{noeldelta.days} jours")


def printElement(cle, valeur) -> None:
    """Print un ensemble cle: valeur"""
    print(f"{cle:>12}:", valeur)


if __name__ == '__main__':
    main()
