import argparse
import os
import requests
import pandas as pd
import time


def get_seasons():
    url = "https://api.nhle.com/stats/rest/en/season?sort=%5B%7B%22property%22:%22id%22,%22direction%22:%22DESC%22%7D%5D"
    response = requests.get(url)
    data = response.json()
    return data["data"]

def get_skaters(report_type, season_id):
    all_players = []
    page = 0
    have_data = True

    while have_data:
        while True:
            url = f"https://api.nhle.com/stats/rest/en/skater/{report_type}?isAggregate=false&isGame=false&start={page * page_size}&limit={page_size}&cayenneExp=gameTypeId=2%20and%20seasonId%3C={season_id}%20and%20seasonId%3E={season_id}"
            response = requests.get(url)
            print(f"{report_type} page {page + 1}  -  response code: {response.status_code}")
            if response.status_code == 429:
                print("Rate limited. Waiting 60 seconds...")
                time.sleep(60)
                continue
            break
        data = response.json()
        have_data = len(data["data"]) > 0
        all_players.extend(data["data"])
        page += 1

    df = pd.json_normalize(all_players)
    filename = f"data/skaters_by_season_{report_type}.csv"
    df.to_csv(
        filename,
        mode="a",  # append
        header=not os.path.exists(filename),  # write header only once
        index=False
    )

parser = argparse.ArgumentParser()
parser.add_argument(
    "--report-type",
    choices=["summary", "bios"],
    default="summary",
    help="Type of skater data to download."
)

parser.add_argument(
    "--start-season",
    type=int,
    help="First season to download (e.g. 20182019). Defaults to earliest available."
)

parser.add_argument(
    "--end-season",
    type=int,
    help="Last season to download (e.g. 20242025). Defaults to latest available."
)

args = parser.parse_args()

seasons = get_seasons()
seasons = sorted(seasons, key=lambda s: s["id"])

if args.start_season:
    seasons = [s for s in seasons if s["id"] >= args.start_season]

if args.end_season:
    seasons = [s for s in seasons if s["id"] <= args.end_season]

season_ids = [s["id"] for s in seasons]

print(f"Scraping {len(season_ids)} seasons: {season_ids}")

page_size = 100

i = 1
for season in seasons:
    season_id = season["id"]
    print(f"Scraping {i}th season: {season_id}")
    get_skaters(args.report_type, season_id)
    i += 1
