import csv
from datetime import datetime

# Fonction pour formater la date
def formater_date(date_str):
    try:
        return datetime.strptime(date_str, '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return date_str  # Laisser la date inchangée si elle n'est pas dans le format attendu

# Charger la deuxième base de données
with open('/Users/mac/Downloads/archive/data/users.csv', 'r', encoding='utf-8') as fichier_entree:
    lecteur = csv.reader(fichier_entree)
    entetes = next(lecteur)  # Obtenir les en-têtes

    # Indiquez ici le chemin vers le fichier de sortie
    with open('/Users/mac/Downloads/archive/data/users_Update.csv', 'w', newline='', encoding='utf-8') as fichier_sortie:
        ecrivain = csv.writer(fichier_sortie, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        ecrivain.writerow(entetes)  # Écrire les en-têtes

        # Parcourir chaque ligne dans la deuxième base de données
        for ligne in lecteur:
            # Réorganiser les colonnes selon la structure de la première base de données
            nouvelle_ligne = [
                ligne[0],  # user_id
                ligne[1],  # location
                ligne[2],  # name
                ligne[3],  # followers_count
                ligne[4],  # statuses_count
                ligne[5],  # time_zone
                ligne[6],  # verified
                ligne[7],  # lang
                ligne[8],  # screen_name
                ligne[9],  # description
                formater_date(ligne[10]) if len(ligne) > 10 else "",  # created_at
                ligne[11],  # favourites_count
                ligne[12],  # friends_count
                ligne[13],  # listed_count
            ]

            # Écrire la nouvelle ligne dans le fichier de sortie
            ecrivain.writerow(nouvelle_ligne)

print("Conversion terminée.")
