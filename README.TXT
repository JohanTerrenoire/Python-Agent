Fonctionnement :
Un agent est installé sur le client et envoi par interval de 5 minutes des données au serveur sous forme d'un dictionnaire Python.

Le serveur réceptionne ces données, crée une base SQLite portant le nom de la machine qui vient de lui envoyer ces informations puis les enregistre dans la base de données.

Lorsqu'un client fait une requête GET pour afficher les données, le serveur lui renvoie une page HTML donc le client n'a pas à mettre en forme les données.

Pour accéder aux information d'une machine, l'URL est du type : http://<SERVER_ADDRESS>:5000/infos/<HOSTNAME>

Si la page "internal server error" appairaît, il peut y avoir deux raisons :
Le serveur n'est pas démarré. 
Le client n'a pas envoyé de données au serveur.
Le nom du HOSTNAME est erroné.

Installation de l'agent (agent.py):
Il faut installer psutil, requests et éventuellement datetime.

Installation du serveur (server.py):
Nécessite FLASK et potentiellement sqlite3

Lancement du serveur : FLASK_APP=server.py flask run
Lancement de l'agent : python agent.py
