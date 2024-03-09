import csv
import ast

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
    # Correction des valeurs de colonnes spécifiques
    # Ajoutez votre logique de correction ici
    ligne["hashtags"] = ast.literal_eval(ligne["hashtags"]) if ligne["hashtags"] else []
    ligne["mentions"] = ast.literal_eval(ligne["mentions"]) if ligne["mentions"] else []
    ligne["expanded_urls"] = ast.literal_eval(ligne["expanded_urls"]) if ligne["expanded_urls"] else []

    # Retourne la ligne corrigée
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
        writer = csv.writer(output_file, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

        # Écrire les en-têtes dans le fichier de sortie
        writer.writerow(list(mapping.values()))

        # Variables pour garder une trace des lignes précédentes
        prev_line = None
        current_line = None

        # Variable pour suivre le nombre de lignes
        line_count = 0

        # Parcourir les lignes du fichier d'entrée
        for line in reader:
            # Vérifier si la première valeur est manquante
            if not line or not line[0]:
                continue  # Ignorer la ligne si la première valeur est manquante

            # Vérifier si la ligne contient un retour à la ligne
            if any('\n' in col for col in line):
                # Ignorer la ligne actuelle et la ligne précédente
                prev_line = None
                current_line = None
                continue

            # Vérifier si le nombre de colonnes est égal au nombre d'en-têtes
            if len(line) == len(headers):
                # Ajouter une paire de guillemets à chaque valeur
                line = [str(value) for value in line]

                # Correction des erreurs entre les bases de données
                ligne_corrigee = corriger_ligne(dict(zip(headers, line)), mapping)
                ligne_corrigee = [str(ligne_corrigee[colonne]) for colonne in mapping.values()]

                # Écrire la ligne dans le fichier de sortie
                writer.writerow(ligne_corrigee)

                # Mettre à jour le nombre de lignes
                line_count += 1

print("Filtrage, ajout de guillemets, correction et écriture des lignes corrigées terminés.")
