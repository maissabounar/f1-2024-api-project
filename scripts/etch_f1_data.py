import requests
import csv

# URL de l'API OpenF1 pour les informations sur les pilotes
url = "https://api.openf1.org/v1/drivers"

# Appel à l'API
response = requests.get(url)
data = response.json()

# Écriture des données dans un fichier CSV
csv_file = "data/drivers.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 'en-tête
    writer.writerow(["driver_number", "broadcast_name", "full_name", "team_name", "country_code"])
    # Écriture des données
    for driver in data:
        writer.writerow([
            driver.get("driver_number"),
            driver.get("broadcast_name"),
            driver.get("full_name"),
            driver.get("team_name"),
            driver.get("country_code")
        ])

print(" Fichier CSV créé dans le dossier data/")
