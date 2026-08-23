from fileinput import filename
import requests
import pandas as pd
import ast



def get_data(url, output_filename):
    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data["data"])
    df.to_csv(
        output_filename,
        index=False
    )

def clean_countries_csv(file_path):
    df = pd.read_csv(file_path)

    provinces = []

    for _, row in df.iterrows():
        if pd.isna(row["stateProvinces"]):
            continue

        state_provinces = ast.literal_eval(row["stateProvinces"])

        for province in state_provinces:
            provinces.append({
                "id": province["id"],
                "country3Code": province["country3Code"],
                "stateProvinceName": province["stateProvinceName"]
            })

    provinces_df = pd.DataFrame(provinces)
    provinces_df.to_csv("data/state_provinces.csv", index=False)

    df = df.drop(
        columns=["imageUrl", "thumbnailUrl", "olympicUrl", "stateProvinces"],
        errors="ignore"
    )

    df.to_csv(file_path, index=False)



def main():
    # retrieve the list of seasons from the NHL API
    url = "https://api.nhle.com/stats/rest/en/season?sort=%5B%7B%22property%22:%22id%22,%22direction%22:%22DESC%22%7D%5D"
    get_data(url, "data/seasons.csv")


    # retrieve the list of teams (franchises) from the NHL API
    url = "https://api.nhle.com/stats/rest/en/franchise?sort=fullName&include=lastSeason.id&include=firstSeason.id"
    get_data(url, "data/teams.csv")

    # retrieve the list of countries from the NHL API
    url = "https://api.nhle.com/stats/rest/en/country?include=stateProvinces&sort=countryName"
    get_data(url, "data/countries.csv")
    clean_countries_csv("data/countries.csv")

    # retrieve the list of drafts from the NHL API
    url = "https://api.nhle.com/stats/rest/en/draft?sort=draftYear"
    get_data(url, "data/drafts.csv")


if __name__ == "__main__":
    main()
