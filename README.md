# Pare-feu Personnel sur Windows avec Python
## Ce projet permet de créer un pare-feu personnalisé sur Windows en utilisant Python. Il permet de surveiller et de bloquer les connexions réseau suspectes, d'envoyer des notifications de sécurité par pop-up ou par email, et d'afficher une interface graphique pour gérer les connexions réseau.

## Table des matières
## Objectif du projet

## Fonctionnalités

## Prérequis

## Installation

## Utilisation

## Améliorations possibles

## Auteurs

## Objectif du projet
Le but de ce projet est de créer un pare-feu personnel pour Windows à l'aide de Python, en offrant des fonctionnalités comme :

Liste des connexions réseau actives.

Blocage d'adresses IP ou de ports spécifiques.

Notifications de sécurité en cas de détection de connexions suspectes (par pop-up ou par email).

Interface graphique (GUI) pour faciliter l'interaction avec l'utilisateur.

Liste noire d'IP pour bloquer automatiquement les connexions suspectes.

Fonctionnalités
Liste des connexions réseau actives
Affiche les connexions réseau actives avec les informations suivantes :

PID du processus.

Adresse locale et distante.

Statut de la connexion.

Blocage des IPs
Permet de bloquer une adresse IP en ajoutant une règle de pare-feu via la commande netsh de Windows.

Notifications de sécurité

Pop-up Windows : Affiche une notification lorsque des connexions suspectes sont détectées.

Email : Envoie un email de notification avec les détails des connexions suspectes.

Interface graphique (GUI)
Utilise Tkinter pour afficher les connexions réseau et permettre à l'utilisateur de bloquer des IPs facilement.

Liste noire d'IP
Vérifie les connexions réseau actives et bloque automatiquement celles provenant d'IP figurant dans une liste noire.

Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

Python 3.x : Télécharge et installe Python depuis python.org.

Bibliothèques Python nécessaires :

psutil : Pour accéder aux informations des connexions réseau.

plyer : Pour les notifications système.

tkinter : Pour l'interface graphique.

smtplib et email : Pour l'envoi de notifications par email.

Vous pouvez installer les bibliothèques Python requises avec la commande suivante :

bash
Copier
Modifier
pip install psutil plyer
Note : Si vous utilisez un serveur SMTP pour envoyer des emails, assurez-vous d'utiliser un mot de passe d'application sécurisé pour votre compte email (ex. : pour Gmail, utilisez un mot de passe d'application).

Installation
Clonez ce dépôt ou téléchargez les fichiers du projet sur votre machine.

Installez les dépendances en exécutant la commande suivante :

bash
Copier
Modifier
pip install psutil plyer
Assurez-vous d'avoir Python 3 installé sur votre machine.

Vérifiez les autorisations d'administrateur pour permettre à Python de manipuler le pare-feu Windows à l'aide de la commande netsh.

Utilisation
Exécution du script
Ouvrez une console (cmd ou PowerShell) en mode administrateur.

Naviguez jusqu'au répertoire contenant le script.

Exécutez le script Python à l'aide de la commande suivante :

bash
Copier
Modifier
python firewall_personal.py
Fonctionnalités principales :
Afficher les connexions réseau actives :

Cliquez sur le bouton "Mettre à jour les connexions" pour voir la liste des connexions actives.

Bloquer une adresse IP :

Sélectionnez une connexion dans la liste, puis cliquez sur "Bloquer l'IP sélectionnée" pour bloquer l'IP associée à cette connexion.

Liste noire d'IP :

Le script vérifie automatiquement les connexions actives et compare les adresses IP aux adresses de la liste noire. Si une correspondance est trouvée, l'IP est bloquée.

Notifications de sécurité :

Si une connexion suspecte est détectée, une notification s'affichera sur votre écran (pop-up) et un email sera envoyé à l'adresse spécifiée.

Interface graphique
L'interface graphique affiche une liste des connexions réseau et offre des boutons pour mettre à jour les connexions et bloquer les IPs sélectionnées.