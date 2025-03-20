import mysql.connector
from config import connect_db  

def add_primary_keys():
    print("\n Adding Primary Keys to Dimension Tables...")

    conn = connect_db()
    cursor = conn.cursor()

    primary_key_queries = [
        "ALTER TABLE dim_orders ADD PRIMARY KEY (order_key);",
        "ALTER TABLE dim_shipping ADD PRIMARY KEY (ship_key);",
        "ALTER TABLE dim_customers ADD PRIMARY KEY (customer_key);",
        "ALTER TABLE dim_regions ADD PRIMARY KEY (region_key);",
        "ALTER TABLE dim_products ADD PRIMARY KEY (product_key);"
    ]

    for query in primary_key_queries:
        cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()
    print(" All primary keys added successfully!")

