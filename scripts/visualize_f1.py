import pandas as pd
import matplotlib.pyplot as plt

# Load the driver data
df = pd.read_csv("data/drivers.csv")

# Drop rows where team_name is missing
df = df.dropna(subset=["team_name"])

# Count number of drivers per team
team_counts = df["team_name"].value_counts()

# Plot the results
plt.figure(figsize=(10, 6))
team_counts.plot(kind="bar")
plt.title("Number of Drivers per Team (F1 2024)")
plt.xlabel("Team")
plt.ylabel("Number of Drivers")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
