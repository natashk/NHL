# NHL Data Collection and Analysis

An end-to-end data project that scrapes, cleans, and analyzes NHL skater statistics — from raw data collection through statistical analysis and visualization.

## Overview

This project reverse-engineers NHL's public API to collect historical skater statistics, then applies statistical analysis and visualization to explore player performance trends.

## Project Structure

```text
NHL/
│
├── data/
│   ├── countries.csv
│   ├── drafts.csv
│   ├── seasons.csv
│   ├── state_provinces.csv
│   ├── teams.csv
│   ├── skaters_by_season_bios.csv
│   └── skaters_by_season_summary.csv
│
├── data_analysis/
│   ├── forward_defence.ipynb
│   └── README.md
│
├── data_scraper/
│   ├── metadata_scraper.py
│   ├── skaters_by_season_scraper.py
│   └── README.md
│
├── README.md
└── requirements.txt
```

- [`data_scraper/`](./data_scraper) — Python scraper that collects all-time regular season skater statistics from the NHL API.
- [`data_analysis/`](./data_analysis) — Jupyter notebooks analyzing the collected data, including statistical testing and visualizations.

See each folder's README for setup instructions and usage details.

## Tech Stack

- **Collection:** Python, Requests, Pandas
- **Analysis:** Python (Jupyter notebooks), Pandas, Matplotlib, SciPy

## Getting Started

1. Clone the repo: `git clone https://github.com/natashk/NHL.git`
2. See [`data_scraper/README.md`](./data_scraper/README.md) to collect fresh data.
3. See [`data_analysis/README.md`](./data_analysis/README.md) to run the analysis notebooks.
