import requests
import csv

# API endpoint to fetch F1 driver information
url = "https://api.openf1.org/v1/drivers"

# Send a GET request to the API
response = requests.get(url)
data = response.json()

# Path to save the CSV file
csv_file = "data/drivers.csv"

# Write the data to a CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write CSV header
    writer.writerow(["driver_number", "broadcast_name", "full_name", "team_name", "country_code"])
    # Write driver data
    for driver in data:
        writer.writerow([
            driver.get("driver_number"),
            driver.get("broadcast_name"),
            driver.get("full_name"),
            driver.get("team_name"),
            driver.get("country_code")
        ])

print(" CSV file created in the data/ folder.")
