# NHL Skater Statistics

## NHL Skater Statistics Scraper

### Overview

This project automates the collection of NHL all-time regular season skater statistics.

The scraper reverse-engineers the NHL website's JSON endpoints to retrieve player statistics, automatically handles pagination and rate limiting, and exports the complete dataset to CSV files for further analysis.
The source of data is the [official NHL website](https://www.nhl.com/stats/skaters).


### Technologies
- Python
- Requests
- Pandas

### Output

The scraper generates:

`data/skaters_bios.csv`
`data/skaters_summary.csv`

Each row represents one NHL player and includes statistics such as:

- player name
- position
- games played
- goals
- assists
- points

and many additional NHL statistics

### Project Structure

    NHL/
    │
    ├── data/
    │   ├── skaters_bios.csv
    │   └── skaters_summary.csv
    ├── data_scraper/
    │   └── skaters_scraper.py
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

```bash
python data_scraper/skaters_scraper.py
```
Output will be saved to `data/skaters_bios.csv` and `data/skaters_summary.csv`.
