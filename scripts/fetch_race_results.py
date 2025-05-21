import requests
import pandas as pd


url = "https://api.openf1.org/v1/results"

#  (filtering by year)
params = {
    "session_key": "qualifying",  
    "year": 2024
}


response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

df.to_csv("../data/race_results_2024.csv", index=False)

print(" Race results saved to data/race_results_2024.csv")
