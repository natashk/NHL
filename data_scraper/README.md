# NHL Data Collection
## Overview

This project collects and prepares NHL data for historical analysis and data visualization.

The project includes two Python-based scrapers:

- **Skater Statistics Scraper** — collects NHL skater statistics by season.
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

## Skater Statistics Scraper

### Overview

The skater statistics scraper collects NHL regular-season skater statistics by season.

The scraper reverse-engineers the NHL website's JSON endpoints to automate data collection. It supports pagination, configurable season ranges, and different report types.

The collected data is saved to CSV files for further analysis.

### Data Types

The scraper supports two report types:

#### Summary

Contains season-level player performance statistics, including:

- Player name
- Position
- Games played
- Goals
- Assists
- Points
- Plus/minus
- Other statistical measures

Output: ```data/skaters_summary.csv```

#### Bios

Contains player biographical and career information, including:

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

Output: ```data/skaters_bios.csv```

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
python data_scraper/skaters_by_season_scraper.py --report-type summmary
```

or

```bash
python data_scraper/skaters_by_season_scraper.py
```

### Scrape player bios for all available seasons

```bash
python data_scraper/skaters_by_season_scraper.py --report-type bios
```

### Scrape a single season (for example 2024-2025):

```bash
python data_scraper/skaters_by_season_scraper.py --report-type summary --start-season 20242025 --end-season 20242025
```

### Scrape a range of seasons (for example, 2018-2019 through 2024-2025):

```bash
python data_scraper/skaters_by_season_scraper.py --report-type bios --start-season 20182019 --end-season 20242025
```

If `--start-season` and `--end-season` are omitted, the scraper downloads data for all available seasons.


### Scrape metadata

```bash
python data_scraper/metadata_scraper.py
```


The generated CSV files are saved in the `data` directory.
