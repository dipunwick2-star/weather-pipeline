import pandas as pd

def transform_weather(df):
    
    df = df.dropna() # remove any rows with missing data
    
    # Convert the time column from string to datetime
    df["time"] = pd.to_datetime(df["time"])

    # add a column for date only
    df["date"] = df["time"].dt.date

    # add a column for hour only
    df["hour"] = df["time"].dt.hour

    # round the columns to 2 decimal places to keep data clean

    df["temperature_c"] = df["temperature_c"].round(2)
    df["humidity_pct"] = df["humidity_pct"].round(2)
    df["wind_speed_kmh"] = df["wind_speed_kmh"].round(2)

    print(f"Transformed {len(df)} rows")
    print(df.head())

    return df


if __name__ == "__main__":

    from extract import fetch_weather
    df = fetch_weather()
    transform_weather(df)