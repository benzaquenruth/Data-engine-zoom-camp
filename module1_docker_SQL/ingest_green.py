import pandas as pd
from sqlalchemy import create_engine

PG_USER = "postgres"
PG_PASSWORD = "postgres"
PG_HOST = "localhost"
PG_PORT = "5433"
PG_DB = "ny_taxi"

PARQUET_FILE = "green_tripdata_2025-11.parquet"
TABLE_NAME = "green_trips_2025_11"

def main():
    engine = create_engine(
        f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
    )

    # Load green trips
    df = pd.read_parquet(PARQUET_FILE)
    df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)
    print(f"Loaded {len(df):,} rows into {TABLE_NAME}")

    # Load taxi zones
    zones_df = pd.read_csv("taxi_zone_lookup.csv")
    zones_df.to_sql("taxi_zone_lookup", con=engine, if_exists="replace", index=False)
    print("Loaded taxi_zone_lookup table")

if __name__ == "__main__":
    main()


