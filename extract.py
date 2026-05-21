import requests
import pandas as pd


def fetch_weather():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 6.93, # GPS coordinate for a chosen City, feel free to change
        "longitude": 79.84,
        # The specific data coloumns  we want back from the API
        # tempertaure, humidity and wind speed as metrics
        "hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "forecast_days": 1 # data for today (24 hours so 24 rows)
    }

    # Send the  GET request to the API with our parameters (like typing into a browser)
    response = requests.get(url, params=params) 

    # convert the response from raw JSON into python directory
    # JSON is the standard format APIs use to send the data back

    data = response.json()

    # the API returns each coloumn as a sperate list inside data["hourly"]
    # pandas DataFrame organises those lists into a table
    # transform step where API data into something clean

    df = pd.DataFrame({
        "time": data["hourly"]["time"], #timestamp for each hour
        "temperature_c": data["hourly"]["temperature_2m"], # temp in celsius, 2m above the ground
        "humidity_pct": data["hourly"]["relative_humidity_2m"], # humidity as a percentage
        "wind_speed_kmh": data["hourly"]["wind_speed_10m"] # wind speed, 10m above the ground
    })

    print(df)

    return df

# runs when you execute this file directory with "python extract.py"
if __name__ == "__main__":
    fetch_weather()