#/usr/bin/env python
# -*- coding:utf-8 -*-

#FLASK_APP=server.py flask run pour lancer le serveur
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/infos/<hostname>", methods=['GET'])
def affiche_info(hostname):
    #Création de la base de données SQLite
    connexion = sqlite3.connect(hostname+'_agent.db')
    cursor = connexion.cursor()
    #Lecture des données et affichage de la page
    cursor.execute("""SELECT * FROM infos WHERE id = (SELECT MAX(id) FROM infos)""")
    resultat = cursor.fetchone()
    print (resultat)
    return render_template('index.html', hostname = resultat[2], os = resultat[4], cpu_count = resultat[1], disque = resultat[5], charge_cpu = resultat[6], memoire_ram = resultat[3], date_maj = resultat[8], boot_time = resultat[7])

@app.route("/api/<hostname>", methods=['POST'])
def recupere_info(hostname):
    #Création de la base de données SQLite
    connexion = sqlite3.connect(hostname+'_agent.db')
    cursor = connexion.cursor()
    #Créer une table si elle n'existe pas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS infos(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         nombre_cpu TEXT,
         nom_machine TEXT,
         utilisation_ram TEXT,
         nom_os TEXT,
         occupation_disque TEXT,
         utilisation_cpu TEXT,
         boot_time TEXT,
         date_maj TEXT);""")
    data = request.form
    cursor.execute("""INSERT INTO infos(nombre_cpu, nom_machine, utilisation_ram, nom_os, occupation_disque, utilisation_cpu, date_maj, boot_time)
                   VALUES(:nombre_cpu, :nom_machine, :utilisation_ram, :nom_os, :occupation_disque, :utilisation_cpu, :date_maj, :boot_time)""", data)
    connexion.commit()
    connexion.close()
    return "Success"
