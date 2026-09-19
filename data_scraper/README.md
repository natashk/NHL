# NHL Data Collection
## Overview

This project collects and prepares NHL data for historical analysis and data visualization.

The project includes three Python-based scrapers:

- **Skaters Statistics Scraper** — collects NHL skater statistics by season.
- **Skaters Bios Scraper** — collects NHL skater bios.
- **Metadata Scraper** — collects reference data such as countries, states and provinces, teams, seasons, and drafts.

The collected data is exported to CSV files and can be used for analysis with Python, SQL, spreadsheets, or data visualization tools.

The source of the data is the [official NHL statistics website](https://www.nhl.com/stats).

## Technologies
- Python
- Requests
- Pandas

## Project Structure

```text
NHL/
│
├── data/
│   ├── countries.csv
│   ├── drafts.csv
│   ├── seasons.csv
│   ├── skaters_bios.csv
│   ├── skaters_by_season_summary.csv
│   ├── state_provinces.csv
│   └── teams.csv
│
├── data_analysis/
│   ├── forward_defence.ipynb
│   └── README.md
│
├── data_scraper/
│   ├── bios_scraper.py
│   ├── metadata_scraper.py
│   ├── skaters_by_season_scraper.py
│   └── README.md
│
├── README.md
└── requirements.txt
```

## Skaters Statistics Scraper

### Overview

The skaters statistics scraper collects NHL regular-season skater statistics by season.

The scraper reverse-engineers the NHL website's JSON endpoints to automate data collection. It supports configurable season ranges.

The collected data is saved to CSV files for further analysis.

Contains season-level player performance statistics, including:

- Player name
- Position
- Games played
- Goals
- Assists
- Points
- Plus/minus
- Other statistical measures

### Output

```data/skaters_summary.csv```


## Skaters Bios Scraper

### Overview

The skaters bios scraper collects player biographical and career information, including:

- Player name
- Position
- Birth date
- Birth country
- Birth state or province
- Nationality
- Draft information
- Height
- Weight
- Hall of Fame status

### Output

```data/skaters_bios.csv```


## Metadata Scraper

### Overview

The metadata scraper collects reference data used to support analysis of the NHL skater datasets.

It retrieves:

- NHL seasons
- Teams
- Countries
- States / Provinces
- NHL drafts

The metadata is saved as separate CSV files.

### Output

```text
data/
├── countries.csv
├── drafts.csv
├── seasons.csv
├── state_provinces.csv
└── teams.csv
```

`countries.csv` - Contains country codes and country names.

`state_provinces.csv` - Contains state and province information extracted from country metadata.

`teams.csv` - Contains NHL team information.

`seasons.csv` - Contains NHL season metadata.

`drafts.csv` - Contains NHL draft metadata.


## Setup

1. Clone the repository
```bash
   git clone https://github.com/natashk/NHL.git
   cd NHL
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```

## Usage

### Scrape summary statistics for all available seasons

```bash
python data_scraper/skaters_by_season_scraper.py
```

### Scrape a single season (for example 2024-2025):

```bash
python data_scraper/skaters_by_season_scraper.py --start-season 20242025 --end-season 20242025
```

### Scrape a range of seasons (for example, 2018-2019 through 2024-2025):

```bash
python data_scraper/skaters_by_season_scraper.py --start-season 20182019 --end-season 20242025
```

If `--start-season` and `--end-season` are omitted, the scraper downloads data for all available seasons.

### Scrape players bios

```bash
python data_scraper/bios_scraper.py
```

### Scrape metadata

```bash
python data_scraper/metadata_scraper.py
```


The generated CSV files are saved in the `data` directory.
