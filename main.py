from create_fact_and_dimensions import create_fact_and_dimension
from load_dimensions import push_to_mysql
from add_primary_keys import add_primary_keys
from create_fact_table import create_fact_table
from create_data_marts import create_data_marts
from calculate_kpis import run_all_kpis
from create_fact_table import process_fact_sales



def main():
    print("\n Starting Supply Chain Data Pipeline...")

    # Step 1: Process Fact & Dimension Tables
    create_fact_and_dimension()

    # Step 2: Load Dimension Tables into MySQL
    push_to_mysql()

    # Step 3: Add Primary Keys
    add_primary_keys()

    print("\n Step 4: Creating & Loading Fact Table...")
    process_fact_sales()

    # Step 5: Create Data Marts
    create_data_marts()

    # Step 6: Run KPIs & Aggregations
    run_all_kpis()

    print("\n Supply Chain Data Pipeline Completed Successfully!")
    


if __name__ == "__main__":
    main()