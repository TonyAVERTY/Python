import socket
import sys
from colorama import Fore, Back, Style

# Création de l'objet socket client
connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3 or sys.argv[1] != '-p': # 3 car il y a script.js -p [port] | 1 car un seul argument
    # Si l'argument n'est pas présent, demander à l'utilisateur de spécifier un port
    print(Back.RED + "Port non spécifié en ligne de commande." + Style.RESET_ALL)
    port_number = input(Fore.GREEN + 'Sur quel port souhaitez-vous vous connecter ? ' + Style.RESET_ALL)
    try:
        port_number = int(port_number)
    except ValueError:
        print(Back.RED + "Le port doit être un entier. Veuillez entrer un nombre valide." + Style.RESET_ALL)
        sys.exit(1)
else:
    # Si l'argument est présent, on utilise celui spécifié
    port_number = int(sys.argv[2])

socket_ip = "127.0.0.1"

connexion_serveur.connect((socket_ip, port_number))
print(Back.GREEN + f"Connecté au serveur {socket_ip} sur le port {port_number}" + Style.RESET_ALL)

while True:
    rep_user = input(Fore.CYAN + "Quel message souhaitez-vous envoyer ? (tapez 'q' ou 'quit' pour quitter)\n")

    # Vérification si l'utilisateur veut quitter la communication
    if rep_user == "quit" or rep_user == "q":
        print(Fore.RED + 'Vous avez mis fin à la communication.')
        connexion_serveur.send("q".encode())  # Envoi de 'exit' au serveur pour fermer la connexion côté serveur
        connexion_serveur.close()
        break
    
    # Vérification si le message n'est pas vide avant de l'envoyer
    elif rep_user:  # Cette condition s'assure que rep_user n'est pas une chaîne vide
        connexion_serveur.send(rep_user.encode())
        rep_server = connexion_serveur.recv(1024)
        message = rep_server.decode('utf-8')
        print(Fore.GREEN + f"Réponse serveur : {message}")
    else:
        print(Back.RED + "Vous ne pouvez pas envoyer un message vide.")
