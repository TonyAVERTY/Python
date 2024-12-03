from random import choice
from colorama import Fore, Style


def afficher_titre():
    print(Style.BRIGHT + "\n------------------------------------")
    print(Fore.CYAN + "🎮 Le jeu du: Pierre - Feuille - Ciseaux 🎮")
    print(Style.BRIGHT + "------------------------------------\n")


def demander_choix():
    try:
        a = int(input(Fore.YELLOW + "Choisissez un chiffre:\n0: 🪨 Pierre\n1: 📄 Feuille\n2: ✂️ Ciseaux\n-> "))
        if a < 0 or a > 2:
            raise ValueError("⚠️ Choix invalide. Vous devez choisir entre 0, 1 ou 2.")
        return a
    except ValueError as e:
        print(Fore.RED + str(e))
        return None


def choix_ordinateur():
    return choice(range(3))


def afficher_resultat(a, b):
    choix = ("🪨 Pierre", "📄 Feuille", "✂️ Ciseaux")
    print("\n{} VS {}".format(Fore.YELLOW + choix[a], Fore.RED + choix[b]))
    if a == b:
        print(Fore.BLUE + "🤝 ÉGALITÉ\n")
    elif (a > b and b + 1 == a) or (a < b and a + b == 2):
        print(Fore.GREEN + "🎉 VOUS GAGNEZ 🎉\n")
    else:
        print(Fore.RED + "💥 VOUS PERDEZ 💥\n")


def demander_rejouer():
    return input(Fore.MAGENTA + "Voulez-vous rejouer ? (y/n): ").lower()


def jeu():
    while True:
        afficher_titre()
        a = None
        while a is None:
            a = demander_choix()

        b = choix_ordinateur()
        afficher_resultat(a, b)

        if demander_rejouer() != 'y':
            print(Fore.MAGENTA + "Au revoir et à bientôt ! 👋")
            break


jeu()
