from urllib import response

import requests
import pandas as pd
import time

page_size = 100

def scrape_nhl_skaters(type):
    all_players = []

    for page in range(0, 79):
        while True:
            print(f"Scraping page {page + 1}")
            url = f"https://api.nhle.com/stats/rest/en/skater/{type}?isAggregate=true&isGame=false&start={page * page_size}&limit={page_size}&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20252026%20and%20seasonId%3E=19171918"
            response = requests.get(url)
            print(f"response code: {response.status_code}")
            if response.status_code == 429:
                print("Rate limited. Waiting 30 seconds...")
                time.sleep(30)
                continue
            break
        data = response.json()
        all_players.extend(data["data"])

        df = pd.json_normalize(all_players)
        df.to_csv(f"data/skaters_{type}.csv", index=False)

scrape_nhl_skaters("summary")
scrape_nhl_skaters("bios")
