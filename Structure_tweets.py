import csv
from datetime import datetime
import json

# Mappage entre les colonnes des deux bases de données
mapping = {
    "user_id": "user_id",
    "user_key": "user_key",
    "created_at": "created_at",
    "created_str": "created_str",
    "retweet_count": "retweet_count",
    "retweeted": "retweeted",
    "favorite_count": "favorite_count",
    "text": "text",
    "tweet_id": "tweet_id",
    "source": "source",
    "hashtags": "hashtags",
    "expanded_urls": "expanded_urls",
    "posted": "posted",
    "mentions": "mentions",
    "retweeted_status_id": "retweeted_status_id",
    "in_reply_to_status_id": "in_reply_to_status_id",
}

# Utilisez ce mapping dans la fonction corriger_ligne
def corriger_ligne(ligne, mapping):
    # Votre logique de correction ici
    # Par exemple, pour l'exemple donné, la ligne n'a pas besoin d'être modifiée
    return ligne

# Chemin du fichier d'entrée
input_file_path = '/Users/mac/Downloads/archive/data/tweets.csv'

# Chemin du fichier de sortie filtré
output_file_path = '/Users/mac/Downloads/archive/data/tweets_filtered.csv'

# Ouvrir le fichier d'entrée en mode lecture
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    # Créer un lecteur CSV
    reader = csv.reader(input_file)

    # Lire les en-têtes
    headers = next(reader)

    # Ouvrir le fichier de sortie en mode écriture
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
        # Créer un écrivain CSV
        writer = csv.writer(output_file)

        # Écrire les en-têtes dans le fichier de sortie
        writer.writerow(list(mapping.values()))

        # Variable pour suivre le nombre de lignes
        line_count = 0

        # Parcourir les lignes du fichier d'entrée
        for line in reader:
            # Vérifier si la première valeur est manquante
            if not line or not line[0]:
                continue  # Ignorer la ligne si la première valeur est manquante

            # Vérifier si la ligne contient un retour à la ligne
            if any('\n' in col for col in line):
                continue  # Ignorer la ligne si elle contient un retour à la ligne

            # Vérifier si le nombre de colonnes est égal au nombre d'en-têtes
            if len(line) == len(headers):
                # Ajouter une paire de guillemets à chaque valeur
                line = [str(value) for value in line]

                # Correction des erreurs entre les bases de données
                ligne_corrigee = corriger_ligne(dict(zip(headers, line)), mapping)

                # Convertir chaque valeur de la ligne corrigée en fonction de son type
                ligne_convertie = []
                for colonne in mapping.values():
                    valeur = ligne_corrigee[colonne]
                    if isinstance(valeur, (list, dict)):  # Convertir les listes et les dictionnaires en chaînes JSON
                        valeur = json.dumps(valeur, ensure_ascii=False)
                    elif isinstance(valeur, datetime):  # Convertir les objets datetime en chaînes
                        valeur = valeur.strftime("%Y-%m-%d %H:%M:%S")

                    ligne_convertie.append(valeur)

                # Écrire la ligne convertie dans le fichier de sortie
                writer.writerow(ligne_convertie)

                # Mettre à jour le nombre de lignes
                line_count += 1

print("Filtrage, correction et écriture des lignes corrigées dans le fichier CSV terminés.")
