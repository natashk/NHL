import os
import requests
import pandas as pd
import time


def get_seasons():
    url = "https://api.nhle.com/stats/rest/en/season?sort=%5B%7B%22property%22:%22id%22,%22direction%22:%22DESC%22%7D%5D"
    response = requests.get(url)
    data = response.json()
    return data["data"]

page_size = 100

def get_skaters(type, season_id):
    all_players = []
    page = 0
    have_data = True

    while have_data:
        while True:
            url = f"https://api.nhle.com/stats/rest/en/skater/{type}?isAggregate=false&isGame=false&start={page * page_size}&limit={page_size}&cayenneExp=gameTypeId=2%20and%20seasonId%3C={season_id}%20and%20seasonId%3E={season_id}"
            response = requests.get(url)
            print(f"{type} page {page + 1}  -  response code: {response.status_code}")
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
    filename = f"data/skaters_by_season_{type}.csv"
    df.to_csv(
        filename,
        mode="a",  # append
        header=not os.path.exists(filename),  # write header only once
        index=False
    )

seasons = get_seasons()
i = 0
for season in seasons:
    season_id = season["id"]
    print(f"Scraping {i}th season: {season_id}")
    get_skaters("summary", season_id)
    i += 1
