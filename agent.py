#/usr/bin/env python
# -*- coding:utf-8 -*-

import psutil
import os
import requests
import time
import datetime

while True:
    #-----Le dictionnaire-----
    info_machine = {}

    #-----Caractéristiques-----

    #Nom de l'OS
    info_machine["nom_os"] = os.name
    #Nom de la machine
    nom_machine = os.uname()
    info_machine["nom_machine"] = nom_machine[1]

    #Nombre de CPU
    info_machine["nombre_cpu"] = psutil.cpu_count()

    #-----Métriques-----

    #Récupération de l'occupation du disque
    res = psutil.disk_usage('/')
    info_machine["occupation_disque"] = res[3]

    #La charge des cpu
    info_machine["utilisation_cpu"] = psutil.cpu_percent()

    #L'occupation de la mémoire ram
    utilisation_ram = psutil.virtual_memory()
    info_machine["utilisation_ram"] = utilisation_ram[2]

    #Ajout de la date
    info_machine["date_maj"] = time.strftime('%d/%m/%y %H:%M',time.localtime())

    #Ajout du boot boot_time
    info_machine["boot_time"] = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")

    #Envoi des données à l'api
    r = requests.post("http://192.168.43.170:5000/api/"+nom_machine[1], data = info_machine)
    print (info_machine)
    time.sleep(300)
pass
