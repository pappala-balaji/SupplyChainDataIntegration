import mysql.connector
import pandas as pd
from config import connect_db  # Import MySQL connection function

#  Function to Load Processed Fact Data from CSV
def load_fact_data():
    fact_sales = pd.read_csv("data/fact_sales.csv")

    # Convert Date Format to `YYYY-MM-DD` for MySQL
    fact_sales['Order Date'] = pd.to_datetime(fact_sales['Order Date'], errors='coerce')
    fact_sales['Ship Date'] = pd.to_datetime(fact_sales['Ship Date'], errors='coerce')

    print(" Fact Sales Data Loaded Successfully!")
    print(fact_sales.isna().sum())  # Show missing values summary
    return fact_sales

#  Function to Create Fact Table in MySQL
def create_fact_table():
    print("\n Creating Fact Table...")

    conn = connect_db()
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS fact_sales (
        `Row ID` INT PRIMARY KEY,
        `Order ID` VARCHAR(50),
        `Customer ID` VARCHAR(50),
        `Product ID` VARCHAR(50),
        `Postal Code` VARCHAR(20),
        `Order Date` DATE,
        `Ship Date` DATE,
        `Sales` DECIMAL(10,4),  
        `order_key` BIGINT,
        `ship_key` BIGINT,
        `customer_key` BIGINT,
        `region_key` BIGINT,
        `product_key` BIGINT,
        FOREIGN KEY (`order_key`) REFERENCES dim_orders(`order_key`),
        FOREIGN KEY (`ship_key`) REFERENCES dim_shipping(`ship_key`),
        FOREIGN KEY (`customer_key`) REFERENCES dim_customers(`customer_key`),
        FOREIGN KEY (`region_key`) REFERENCES dim_regions(`region_key`),
        FOREIGN KEY (`product_key`) REFERENCES dim_products(`product_key`)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()
    print(" Fact table `fact_sales` created successfully!")

#  Function to Insert Data into MySQL
def insert_fact_data():
    fact_sales = load_fact_data()  # Load CSV data

    conn = connect_db()
    cursor = conn.cursor()

    # Wrap Column Names in Backticks for MySQL
    columns = ', '.join([f"`{col}`" for col in fact_sales.columns])
    placeholders = ', '.join(['%s'] * len(fact_sales.columns))
    sql = f"INSERT INTO fact_sales ({columns}) VALUES ({placeholders})"

    # Convert DataFrame to List of Tuples
    data = [tuple(row) for _, row in fact_sales.iterrows()]

    try:
        cursor.executemany(sql, data)
        conn.commit()
        print(" Data inserted into `fact_sales` successfully!")
    except mysql.connector.Error as e:
        print(f" Error inserting data: {e}")

    cursor.close()
    conn.close()

#  Function to Run Fact Table Creation and Data Loading
def process_fact_sales():
    create_fact_table()
    insert_fact_data()
