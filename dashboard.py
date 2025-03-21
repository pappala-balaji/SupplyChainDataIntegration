import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from calculate_kpis import (
    sales_growth, 
    top_selling_products, 
    total_sales_by_region, 
    inventory_analysis, 
    order_fulfillment, 
    shipping_logistics,
    total_avg_sales, 
    sales_by_category
)

# Set Streamlit Page Configuration
st.set_page_config(page_title="Supply Chain Dashboard", layout="wide")

# Title
st.title(" Supply Chain Data Integration Dashboard")

#Sidebar Navigation
st.sidebar.header(" Select Analysis Type")
options = ["Project Summary", "Schema Diagram", "KPI Analysis", "Data Mart Analysis", "Aggregations"]
selected_option = st.sidebar.radio("Choose an option", options)

#Project Summary
if selected_option == "Project Summary":
    st.markdown("""
    ### **Project Overview**
    This project focuses on integrating, analyzing, and visualizing **Supply Chain Data** using **Python, MySQL, and Streamlit**.
    - **ETL Process:** Extract, Clean, and Load data into a structured **Star Schema**.
    - **Database Design:** Divided data into **Fact Table (`fact_sales`)** and multiple **Dimension Tables**.
    - **KPI Analysis:** Sales trends, Top Products, Sales by Region, etc.
    - **Data Marts:** Inventory, Order Fulfillment, Shipping Analysis.
    - **Visualization:** Interactive Streamlit dashboard with tables and charts.
    """)

# Schema Diagram
elif selected_option == "Schema Diagram":
    st.subheader(" Supply Chain Database Schema")
    st.image("Schema.png", use_container_width=True)

#  KPI Analysis Section
elif selected_option == "KPI Analysis":
    st.sidebar.subheader(" Select a KPI")
    
    kpi_options = {
        " Total Sales by Year": sales_growth,
        " Top 5 Best-Selling Products": top_selling_products,
        " Total Sales by Region": total_sales_by_region
    }
    
    selected_kpi = st.sidebar.radio("Choose a KPI", list(kpi_options.keys()))

    #  Display KPI Result on Right Side
    st.subheader(f"{selected_kpi} Results")
    df = kpi_options[selected_kpi]()  # Run selected KPI function
    st.dataframe(df)  # Show DataFrame in table format

    #  Graphs for KPIs using Matplotlib & Seaborn
    fig, ax = plt.subplots(figsize=(10, 5))

    if selected_kpi == " Total Sales by Year":
        sns.lineplot(data=df, x="year", y="total_sales", marker="o", ax=ax)
        ax.set_title("Sales Over the Years")
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Sales")

    elif selected_kpi == " Top 5 Best-Selling Products":
        sns.barplot(data=df, x="total_sales", y="Product Name", ax=ax, palette="viridis")
        ax.set_title("Top 5 Selling Products")
        ax.set_xlabel("Total Sales")
        ax.set_ylabel("Product Name")

    elif selected_kpi == " Total Sales by Region":
        sns.barplot(data=df, x="Region", y="total_sales", ax=ax, palette="coolwarm")
        ax.set_title("Total Sales by Region")
        ax.set_xlabel("Region")
        ax.set_ylabel("Total Sales")

    st.pyplot(fig)  # Display plot in Streamlit


#  Data Mart Analysis Section**
elif selected_option == "Data Mart Analysis":
    st.sidebar.subheader(" Select a Data Mart")

    data_mart_options = {
        " Inventory Analysis": inventory_analysis,
        " Order Fulfillment": order_fulfillment,
        " Shipping & Logistics": shipping_logistics
    }

    selected_mart = st.sidebar.radio("Choose a Data Mart", list(data_mart_options.keys()))

    #  Display Data Mart on Right Side
    st.subheader(f"{selected_mart} Results")
    df = data_mart_options[selected_mart]()  # Run selected Data Mart function
    st.dataframe(df)  # Show DataFrame in table format

  #Aggregations Section

elif selected_option == "Aggregations":
    st.sidebar.subheader(" Select Aggregation")

    agg_options = {
        " Total & Average Sales": total_avg_sales,
        " Sales by Category": sales_by_category
    }

    selected_agg = st.sidebar.radio("Choose an Aggregation", list(agg_options.keys()))

    #  Display Aggregation Data
    st.subheader(f"{selected_agg} Results")
    df = agg_options[selected_agg]()  # Run Aggregation function
    st.dataframe(df)

    #  Graph only for Sales by Category
    if selected_agg == " Sales by Category":
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=df, x="total_sales", y="Category", ax=ax, palette="Blues")
        ax.set_title("Total Sales by Product Category")
        ax.set_xlabel("Total Sales")
        ax.set_ylabel("Category")
        st.pyplot(fig)

    #  Display Text Summary for Total & Average Sales (No Graph)
    elif selected_agg == " Total & Average Sales":
        st.write(f" **Total Sales:** {df['total_sales'][0]:,.2f}")
        st.write(f" **Average Order Value:** {df['avg_order_value'][0]:,.2f}")
