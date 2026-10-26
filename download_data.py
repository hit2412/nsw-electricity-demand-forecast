import requests
import os

os.makedirs("data/raw", exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}

for year in [2024, 2025]:
    for month in range(1, 13):
        ym = f"{year}{month:02d}"
        filename = f"PRICE_AND_DEMAND_{ym}_NSW1.csv"
        url = f"https://aemo.com.au/aemo/data/nem/priceanddemand/{filename}"

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open(f"data/raw/{filename}", "wb") as f:
                f.write(response.content)
            print("Downloaded", filename)
        else:
            print("Failed", filename, response.status_code)