# Weather Pipeline

A simple ETL data pipeline that fetches live weather data and stores it in PostgreSQL.

## What it does
- Fetches hourly weather data for any location in the world using coordinates
- Cleans and transforms the data using pandas
- Loads it into a PostgreSQL database
- Runs automatically every hour

## Project Structure
- `extract.py` → fetches data from the Open-Meteo API
- `transform.py` → cleans and shapes the data
- `load.py` → writes data to PostgreSQL
- `pipeline.py` → runs everything together on a schedule

## Tools Used
- Python
- pandas
- requests
- SQLAlchemy
- PostgreSQL
- schedule

## How to run
1. Install dependencies: `pip install -r requirements.txt`
2. Create a PostgreSQL database called `weather_db`
3. Update the password in `load.py`
4. Update the `latitude` and `longitude` in `extract.py` to your desired location
5. Run the pipeline: `python pipeline.py`