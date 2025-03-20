# README: Supply Chain Data Integration System

## 📌 Project Overview
This project focuses on **supply chain data integration** using **Python, MySQL, and Streamlit**. The goal is to **clean, integrate, and analyze** supply chain data using a **Star Schema approach**, enabling effective insights through **KPIs, Data Marts, and interactive visualizations**.

## 🔗 Data Source
- **Dataset:** Global Superstore Dataset (Orders, Customers, Products, Shipping)

## 📂 Project Flow
### 1️⃣ Data Cleaning & Preprocessing
- Handled **missing values**, corrected **data types**, and removed **duplicates**.

### 2️⃣ Star Schema Design
- Divided data into **Fact Table (`fact_sales`)** and **Dimension Tables (`dim_customers`, `dim_products`, etc.)**.
- Used **Surrogate Keys** to enhance relationships and analytics.

### 3️⃣ Data Loading into MySQL
- **Loaded Dimension Tables first**, then altered them by adding **Primary Keys**.
- Created & loaded **Fact Table (`fact_sales`)**.

### 4️⃣ Data Marts & KPIs Calculation
- Built **Inventory, Order Fulfillment, and Shipping Data Marts**.
- Calculated **Key KPIs** like **Sales Trends
 and Product Performance**.

### 5️⃣ Interactive Dashboard (Streamlit)
- Developed an **interactive Streamlit Dashboard** to visualize **KPIs and Data Marts**.

## 🛠️ Tech Stack Used
✅ **Python** – Data Processing & Analysis  
✅ **MySQL** – Database Management  
✅ **SQLAlchemy / MySQL Connector** – For SQL operations  
✅ **Pandas & NumPy** – Data Manipulation  
✅ **Matplotlib & Seaborn** – Data Visualization  
✅ **Streamlit** – Interactive Dashboard  

## 📂 How to Set Up & Run the Project
### 1️⃣ Set Up Virtual Environment (Optional)
```sh
python -m venv myenv
myenv\Scripts\activate  # Windows
source env/bin/activate  # macOS/Linux
```

### 2️⃣ Clone the Repository
```sh
https://github.com/pappala-balaji/SupplyChainDataIntegration.git
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Project
```sh
streamlit run dashboard.py
```
