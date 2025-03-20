import pandas as pd
from config import connect_db  

def run_query(query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    return pd.DataFrame(data, columns=columns)

# KPI 1: Sales Growth Over Years
def sales_growth():
    query = """
    SELECT YEAR(`Order Date`) AS year, 
           SUM(Sales) AS total_sales
    FROM fact_sales
    GROUP BY YEAR(`Order Date`)
    ORDER BY year;
    """
    return run_query(query)

# KPI 2: Top 5 Best-Selling Products
def top_selling_products():
    query = """
    SELECT p.`Product Name`, SUM(f.Sales) AS total_sales
    FROM fact_sales f
    JOIN dim_products p ON f.product_key = p.product_key
    GROUP BY p.`Product Name`
    ORDER BY total_sales DESC
    LIMIT 5;
    """
    return run_query(query)

# KPI 3: Total Sales by Region
def total_sales_by_region():
    query = """
    SELECT r.`Region`, SUM(f.Sales) AS total_sales
    FROM fact_sales f
    JOIN dim_regions r ON f.region_key = r.region_key
    GROUP BY r.`Region`
    ORDER BY total_sales DESC;
    """
    return run_query(query)

# Data Mart 1: Inventory Analysis
def inventory_analysis():
    query = "SELECT * FROM mart_inventory_analysis LIMIT 20;"
    return run_query(query)

# Data Mart 2: Order Fulfillment
def order_fulfillment():
    query = "SELECT * FROM mart_order_fulfillment LIMIT 20;"
    return run_query(query)

# Data Mart 3: Shipping and Logistics
def shipping_logistics():
    query = "SELECT * FROM mart_shipping_logistics LIMIT 20;"
    return run_query(query)

# Aggregation 1: Total & Average Sales
def total_avg_sales():
    query = """
    SELECT 
        SUM(Sales) AS total_sales, 
        AVG(Sales) AS avg_order_value 
    FROM fact_sales;
    """
    return run_query(query)

# Aggregation 2: Sales by Product Category
def sales_by_category():
    query = """
    SELECT p.Category, SUM(f.Sales) AS total_sales
    FROM fact_sales f
    JOIN dim_products p ON f.product_key = p.product_key
    GROUP BY p.Category
    ORDER BY total_sales DESC;
    """
    return run_query(query)

def run_all_kpis():
    print("\n Running KPI Analysis...")
    print("\n Sales Growth by Year:")
    print(sales_growth())

    print("\n Top 5 Best-Selling Products:")
    print(top_selling_products())

    print("\n Total Sales by Region:")
    print(total_sales_by_region())

    print("\n Running Data Mart Analysis...")
    print("\n Inventory Analysis:")
    print(inventory_analysis().head())

    print("\n Order Fulfillment:")
    print(order_fulfillment().head())

    print("\n Shipping and Logistics:")
    print(shipping_logistics().head())

    print("\n Running Aggregation Metrics...")
    print("\n Total & Average Sales:")
    print(total_avg_sales())

    print("\n Sales by Category:")
    print(sales_by_category())

    print("\n KPI & Data Mart Analysis Completed Successfully!")

