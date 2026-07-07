# NHL Skater Statistics

## NHL Skater Statistics Scraper

### Overview

This project automates the collection of NHL regular season skater statistics by season.

The scraper reverse-engineers the NHL website's JSON endpoints to retrieve player statistics, automatically handles pagination and HTTP 429 (Too Many Requests) responses, and exports the data to CSV files for further analysis.

The source of the data is the [official NHL statistics website](https://www.nhl.com/stats/skaters).

### Technologies
- Python
- Requests
- Pandas

### Output

The scraper generates one CSV file per run, depending on the selected report type:

- `data/skaters_by_season_bios.csv`  for summary reports
- `data/skaters_by_season_summary.csv` for bios reports

Each row represents one NHL player for a specific season.

### Project Structure

    NHL/
    │
    ├── data/
    │   ├── skaters_by_season_bios.csv
    │   └── skaters_by_season_summary.csv
    ├── data_scraper/
    │   └── skaters_by_season_scraper.py
    ├── README.md
    └── requirements.txt

### Setup

1. Clone the repository
```bash
   git clone https://github.com/natashk/NHL.git
   cd NHL
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```

### Usage

Download summary statistics for all available seasons:

```bash
python data_scraper/skaters_by_season_scraper.py --report-type summmary
```

or

```bash
python data_scraper/skaters_by_season_scraper.py
```

Download player bios for all available seasons:

```bash
python data_scraper/skaters_by_season_scraper.py --report-type bios
```

Download summary statistics for a single season (for example 2024-2025):

```bash
python data_scraper/skaters_by_season_scraper.py --report-type summary --start-season 20242025 --end-season 20242025
```

Download player bios for a range of seasons (for example, 2018-2019 through 2024-2025):

```bash
python data_scraper/skaters_by_season_scraper.py --report-type bios --start-season 20182019 --end-season 20242025
```

If `--start-season` and `--end-season` are omitted, the scraper downloads data for all available seasons.

The generated CSV files are saved in the data directory.
