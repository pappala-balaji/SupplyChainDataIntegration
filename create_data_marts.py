import mysql.connector
from config import connect_db  # Import MySQL connection function

import mysql.connector
from config import connect_db  # Import MySQL connection function

#  Function to create Data Marts in MySQL
def create_data_marts():
    conn = connect_db()
    cursor = conn.cursor()

    #  Data Mart 1: Inventory Analysis
    inventory_query = """
    CREATE TABLE IF NOT EXISTS mart_inventory_analysis AS
    SELECT  
        p.product_key,  
        p.`Product ID`,  
        p.`Category`,  
        p.`Sub-Category`,  
        COUNT(DISTINCT f.order_key) AS total_orders,  
        SUM(f.Sales) AS total_sales_revenue  
    FROM fact_sales f  
    JOIN dim_products p ON f.product_key = p.product_key  
    GROUP BY  
        p.product_key, p.`Product ID`, p.Category, p.`Sub-Category`;
    """
    cursor.execute(inventory_query)
    print(" Data Mart `mart_inventory_analysis` created.")

    # Data Mart 2: Order Fulfillment
    order_fulfillment_query = """
    CREATE TABLE IF NOT EXISTS mart_order_fulfillment AS
    SELECT 
        f.order_key,
        d.`Order ID` AS order_id,
        c.`Customer ID` AS customer_id,
        c.`Customer Name` AS customer_name,
        p.`Product Name` AS product_name,
        r.`Region` AS region_name,  
        SUM(f.Sales) AS total_sales,
        COUNT(f.order_key) AS total_orders
    FROM fact_sales f
    LEFT JOIN dim_orders d ON f.order_key = d.order_key
    LEFT JOIN dim_customers c ON f.customer_key = c.customer_key
    LEFT JOIN dim_products p ON f.product_key = p.product_key
    LEFT JOIN dim_regions r ON f.region_key = r.region_key  
    GROUP BY f.order_key, order_id, customer_id, customer_name, product_name, region_name;
    """
    cursor.execute(order_fulfillment_query)
    print(" Data Mart `mart_order_fulfillment` created.")

    #  Data Mart 3: Shipping and Logistics
    shipping_logistics_query = """
    CREATE TABLE IF NOT EXISTS mart_shipping_logistics AS
    SELECT 
        f.order_key,
        d.`Order ID` AS order_id,
        c.`Customer ID` AS customer_id,
        c.`Customer Name` AS customer_name,
        r.`Region` AS region_name,
        s.`Ship Mode` AS ship_mode,
        SUM(f.Sales) AS total_sales,
        COUNT(f.order_key) AS total_orders,
        AVG(DATEDIFF(f.`Ship Date`, f.`Order Date`)) AS avg_shipping_days
    FROM fact_sales f
    LEFT JOIN dim_orders d ON f.order_key = d.order_key
    LEFT JOIN dim_customers c ON f.customer_key = c.customer_key
    LEFT JOIN dim_regions r ON f.region_key = r.region_key
    LEFT JOIN dim_shipping s ON f.ship_key = s.ship_key
    GROUP BY f.order_key, order_id, customer_id, customer_name, region_name, ship_mode;
    """
    cursor.execute(shipping_logistics_query)
    print(" Data Mart `mart_shipping_logistics` created.")

    conn.commit()
    cursor.close()
    conn.close()
    print(" All Data Marts Created Successfully!")

