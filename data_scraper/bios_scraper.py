import skaters_by_season_scraper as skaters_scraper
import pandas as pd

def clean_skaters_bios_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.drop(
        columns=["assists", "gamesPlayed", "goals", "points"],
        errors="ignore"
    )
    df = df.drop_duplicates()
    df.to_csv(file_path, index=False)
    df.to_csv("data/skaters_bios.csv", index=False)


def main():
    seasons = skaters_scraper.get_seasons()
    print(f"Found {len(seasons)} seasons: {[s['id'] for s in seasons]}")

    report_type = "bios"
    filename = f"data/skaters_{report_type}.csv"
    i = 1
    for season in seasons:
        season_id = season["id"]
        print(f"Scraping {i}th season: {season_id}")
        skaters_scraper.get_skaters(report_type, season_id, filename)
        i += 1
    clean_skaters_bios_csv(filename)


if __name__ == "__main__":
    main()
