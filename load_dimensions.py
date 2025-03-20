import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

def push_to_mysql():
    print("\n Loading Dimension Tables into MySQL...")

    load_dotenv()
    DB_USERNAME = os.getenv("USER")
    DB_PASSWORD = os.getenv("PASSWORD")
    DB_HOST = "localhost"
    DB_NAME = "supplychaindataintegration"

    engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

    # Load CSV files
    tables = {
        "dim_orders": pd.read_csv("data/dim_orders.csv"),
        "dim_shipping": pd.read_csv("data/dim_shipping.csv"),
        "dim_customers": pd.read_csv("data/dim_customers.csv"),
        "dim_regions": pd.read_csv("data/dim_regions.csv"),
        "dim_products": pd.read_csv("data/dim_products.csv"),
    }

    for table_name, df in tables.items():
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f" {table_name} loaded successfully!")

