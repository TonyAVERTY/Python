import socket
import argparse
from colorama import Fore, Back, Style

parser = argparse.ArgumentParser(description="Serveur socket qui écoute sur un port donné. Le port par défaut est 9000.")

parser.add_argument("-p", "--port", default="9000", help="Port sur lequel le serveur doit écouter (par défaut 9000).")
args=parser.parse_args()

# Création de l'objet socket serveur
socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Demander quel port le serveur doit écouter
port_number = args.port
socket_ip = "127.0.0.1"
port_number = int(port_number)

# Lier l'adresse IP et le port
socket_ecoute.bind((socket_ip, port_number))

# Commencer à écouter les connexions
socket_ecoute.listen()
print(Fore.GREEN + f"Le serveur est bien lancé sur {socket_ip}:{port_number}")

# Accepter la connexion d'un client dans une boucle
while True:
    connexion_client, adresse_client = socket_ecoute.accept()
    print(Fore.MAGENTA +f"Connexion établie avec {adresse_client}")

    while True:
        # Recevoir le message du client
        rep_user = connexion_client.recv(1024)

        if not rep_user:  # Si aucune donnée n'est reçue, le client a fermé la connexion
            print(Fore.RED + 'Le client a fermé la connexion.')
            connexion_client.close()
            break  # Sortir de la boucle while pour accepter un autre client
        
        message = rep_user.decode('utf-8')  # Décoder le message en UTF-8
        if message == "q" or message.lower() == "quit":  # Si le client envoie 'exit' ou 'quit'
            print(Fore.RED + 'Le client a mis fin à la communication.')
            connexion_client.close()
            break  # Sortir de la boucle while pour accepter un autre client
        if rep_user:
            print(Fore.GREEN + f"Réponse utilisateur ({adresse_client}): {message}")
            rep_server = input(Fore.CYAN + "Quel réponse souhaitez-vous envoyer ?\n")
            connexion_client.send(rep_server.encode())

    # Reprise de l'écoute pour un autre client après la fermeture de la connexion
    print(f"En attente d'une nouvelle connexion sur {socket_ip}:{port_number}")