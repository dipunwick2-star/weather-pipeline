import schedule
import time
from extract import fetch_weather
from transform import transform_weather
from load import load_weather

def run_pipeline():

    print("Pipeline starting...")

    #step 1 - extract

    df = fetch_weather()

    # step 2 - transform

    df = transform_weather(df)

    # step 3 - load

    load_weather(df)

    print("Pipeline complete!")


run_pipeline()

# then run every hour automatically 
schedule.every(1).minutes.do(run_pipeline)

print("Pipeline is running evry hour. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(60) # check every 60 seconds if a job is