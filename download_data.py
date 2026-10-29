import requests
import os

os.makedirs("data/raw", exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}


# ---------- Electricity demand data (AEMO) ----------

for year in [2024, 2025]:
    for month in range(1, 13):
        ym = f"{year}{month:02d}"
        filename = f"PRICE_AND_DEMAND_{ym}_NSW1.csv"

        if os.path.exists(f"data/raw/{filename}"):
            continue

        url = f"https://aemo.com.au/aemo/data/nem/priceanddemand/{filename}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open(f"data/raw/{filename}", "wb") as f:
                f.write(response.content)
            print("Downloaded", filename)
        else:
            print("Failed", filename, response.status_code)


# ---------- Weather data (Open-Meteo) ----------

weather_url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": -33.87,
    "longitude": 151.21,
    "start_date": "2024-01-01",
    "end_date": "2025-12-31",
    "hourly": "temperature_2m,relative_humidity_2m",
    "timezone": "Australia/Brisbane"
}

response = requests.get(weather_url, params=params)

if response.status_code == 200:
    with open("data/raw/weather_sydney.json", "wb") as f:
        f.write(response.content)
    print("Downloaded weather_sydney.json")
else:
    print("Failed weather", response.status_code)