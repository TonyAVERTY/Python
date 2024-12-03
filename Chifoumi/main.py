from random import choice
from colorama import Fore, Style


choix = ("🪨 Pierre", "📄 Feuille", "✂️ Ciseaux") # Définir la pierre, la feuille, et les ciseaux

while True:
 
    
    print(Style.BRIGHT + "\n------------------------------------")
    print(Fore.CYAN + "🎮 Le jeu du: Pierre - Feuille - Ciseaux 🎮") # Titre du jeu.
    print(Style.BRIGHT + "------------------------------------\n")
 
    
    try:
        a = int(input(Fore.YELLOW + "Choisissez un chiffre:\n0: 🪨 Pierre\n1: 📄 Feuille\n2: ✂️ Ciseaux\n-> ")) # Demande à l'utilisateur de choisir un chiffre
        if a < 0 or a > 2:
            raise ValueError("⚠️ Choix invalide. Vous devez choisir entre 0, 1 ou 2.")
    except ValueError as e:
        print(Fore.RED + str(e))
        continue
    
    
    b = choice(range(3)) # Choix aléatoire de l'ordinateur

    
    print("\n{} VS {}".format(Fore.YELLOW + choix[a], Fore.RED + choix[b])) # Afficher le choix user et computer

    # Vérification du résultat du jeu
    if a == b:
        print(Fore.BLUE + "🤝 ÉGALITÉ\n") # Égalité
    elif (a > b and b + 1 == a) or (a < b and a + b == 2):
        print(Fore.GREEN + "🎉 VOUS GAGNEZ 🎉\n") # Victoire
    else:      
        print(Fore.RED + "💥 VOUS PERDEZ 💥\n") # Défaite

    
    rejouer = input(Fore.MAGENTA + "Voulez-vous rejouer ? (y/n): ").lower() # Demander si l'utilisateur veut rejouer
    if rejouer != 'y':
        print(Fore.MAGENTA + "Au revoir et à bientôt ! 👋")
        break
