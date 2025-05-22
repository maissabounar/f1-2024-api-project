# F1 2024 Data Project

This project is a personal exploration of Formula 1 data from the 2024 season.  
I used the [OpenF1 API](https://openf1.org/) to collect real-time data and built an analysis pipeline with Python and Jupyter Notebook.

## Why this project?

I'm a Digital Data Analyst and I wanted to challenge myself with something both fun and technical.  
Formula 1 is a great playground: it's fast, dynamic, and full of structured data.

The goal was to create a simple data pipeline that:
- Ingests data from an open API
- Stores and transforms the data
- Explores it through visualizations
- Prepares for dashboarding

## Data Source

All data comes from [openf1.org](https://openf1.org/), a free API providing:
- Driver profiles
- Race results
- Lap times
- Telemetry and sessions (planned)

## Project structure

f1-2024-api-project/
│
├── data/ # CSV files exported from the API
├── scripts/ # Python scripts for data ingestion and visualization
│ ├── fetch_f1_data.py
│ └── fetch_race_results.py
├── notebooks/ # Jupyter Notebook for analysis
│ └── f1_analysis.ipynb
├── requirements.txt # Python dependencies
└── README.md # You are here


## How to use this project

1. Clone the repository:
git clone https://github.com/your-username/f1-2024-api-project.git
cd f1-2024-api-project

2. Install the requirements:
pip install -r requirements.txt


3. Run the data ingestion scripts:
python scripts/fetch_f1_data.py
python scripts/fetch_race_results.py

4. Open the notebook:
jupyter notebook notebooks/f1_analysis.ipynb


## Visualizations

The notebook includes:
- Bar charts showing the number of drivers per team
- Exploratory views of the 2024 race results (to be expanded)

## What's next?

I plan to:
- Add lap time data and build a pace evolution chart per driver
- Create an interactive dashboard using Plotly or Dash
- Explore qualifying sessions and compare driver performances

## About me

I work as a Digital Data Analyst and enjoy building technical side projects to improve my skills in data engineering, analytics, and Python development.

If you have feedback or suggestions, feel free to reach out.
