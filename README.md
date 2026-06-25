# NHL Skater Statistics

## NHL Skater Statistics Scraper

### Overview

This project automates the collection of NHL all-time regular season skater statistics.

The scraper reverse-engineers the NHL website's (https://www.nhl.com/stats/skaters) JSON endpoints to retrieve player statistics, automatically handles pagination and rate limiting, and exports the complete dataset to a CSV file for further analysis.


### Technologies
- Python
- Requests
- Pandas

### Output

data/nhl_skaters.csv

Each row represents one NHL player and includes statistics such as:

Player name
Team
Position
Games Played
Goals
Assists
Points
Plus/Minus
Penalty Minutes
Time on Ice
and many additional NHL statistics

### Installation
git clone https://github.com/natashk/NHL.git
cd NHL

pip install -r requirements.txt

### Usage

Run the scraper:

python skaters_scraper.py

The CSV file will be created in the *data* directory.