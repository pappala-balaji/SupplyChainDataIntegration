import pandas as pd

def create_fact_and_dimension():
    print("\n Creating Fact & Dimension Tables...")

    # Load Data
    df = pd.read_csv("data/data.csv")

    # Handle Missing Postal Code
    df['Postal Code'] = df['Postal Code'].fillna(df['Postal Code'].mode()[0])

    # Convert Dates to DateTime Format
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y")

    # Create Dimension Tables
    dim_orders = df[['Order ID', 'Order Date']].drop_duplicates().reset_index(drop=True)
    dim_orders.insert(0, 'order_key', range(1, len(dim_orders) + 1))

    dim_shipping = df[['Ship Date', 'Ship Mode']].drop_duplicates().reset_index(drop=True)
    dim_shipping.insert(0, 'ship_key', range(1, len(dim_shipping) + 1))

    dim_customers = df[['Customer ID', 'Customer Name', 'Segment']].drop_duplicates().reset_index(drop=True)
    dim_customers.insert(0, 'customer_key', range(1, len(dim_customers) + 1))

    dim_regions = df[['Country', 'City', 'State', 'Region', 'Postal Code']].drop_duplicates().reset_index(drop=True)
    dim_regions.insert(0, 'region_key', range(1, len(dim_regions) + 1))

    dim_products = df[['Product ID', 'Category', 'Sub-Category', 'Product Name']].drop_duplicates().reset_index(drop=True)
    dim_products.insert(0, 'product_key', range(1, len(dim_products) + 1))

    # Create Fact Table
    fact_sales = df[['Row ID', 'Order ID', 'Customer ID', 'Product ID', 'Postal Code', 'Order Date', 'Ship Date', 'Sales']].copy()

    # Map Surrogate Keys
    fact_sales['order_key'] = fact_sales['Order ID'].map(dict(zip(dim_orders['Order ID'], dim_orders['order_key'])))
    fact_sales['ship_key'] = fact_sales['Ship Date'].map(dict(zip(dim_shipping['Ship Date'], dim_shipping['ship_key'])))
    fact_sales['customer_key'] = fact_sales['Customer ID'].map(dict(zip(dim_customers['Customer ID'], dim_customers['customer_key'])))
    fact_sales['region_key'] = fact_sales['Postal Code'].map(dict(zip(dim_regions['Postal Code'], dim_regions['region_key'])))
    fact_sales['product_key'] = fact_sales['Product ID'].map(dict(zip(dim_products['Product ID'], dim_products['product_key'])))

    # Save to CSV
    dim_orders.to_csv("data/dim_orders.csv", index=False)
    dim_shipping.to_csv("data/dim_shipping.csv", index=False)
    dim_customers.to_csv("data/dim_customers.csv", index=False)
    dim_regions.to_csv("data/dim_regions.csv", index=False)
    dim_products.to_csv("data/dim_products.csv", index=False)
    fact_sales.to_csv("data/fact_sales.csv", index=False)

    print(" Fact & Dimension Tables Created and Saved!")

