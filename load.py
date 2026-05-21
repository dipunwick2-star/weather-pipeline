from sqlalchemy import create_engine

def load_weather(df):
    #create connection to your PostgreSQL database

    engine = create_engine("postgresql://postgres:PASSWORD@localhost:5432/weather_db")


    #write a dataframe to a table called "weather"
    # if_exists = "append" mean new rows get added each time


    df.to_sql(
        name="weather", # table name in PostgreSQL
        con=engine,     # the connection
        if_exists="append", # add rows each run
        index=False 
    )

    print(f"Loaded {len(df)} rows into PostgreSQL")


if __name__ == "__main__":

    from extract import fetch_weather
    from transform import transform_weather

    df = fetch_weather()
    df = transform_weather(df)
    load_weather(df)