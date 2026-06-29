# 🛒 E-Commerce Medallion Data Pipeline

An end-to-end data engineering pipeline implementing the Medallion Architecture (Bronze, Silver, Gold) in Azure Databricks. This project processes large-scale e-commerce datasets to generate business-ready analytics.

## 🏗️ Architecture Overview
The pipeline is designed to incrementally ingest, clean, and aggregate raw e-commerce data from Azure Data Lake Storage (ADLS).

1. **Bronze (Raw)**: Ingestion of raw `.csv` files (`customers_big.csv`, `orders_big.csv`, `products_big.csv`).
2. **Silver (Enriched)**: Data cleansing, deduplication, and schema enforcement using PySpark.
3. **Gold (Curated)**: Aggregated tables optimized for business intelligence and reporting.

## 📁 Repository Structure

* **`Data/`**: Contains the raw datasets (Customers, Orders, Products).
* **`Images/`**: Visualizations and dashboard screenshots showcasing the final metrics.
* **`Notebooks/`**:
  * `01_bronze_ingestion_orders.ipynb`: Handles Auto Loader and raw data ingestion.
  * `02_silver_transformations.ipynb`: Core ETL logic, data type casting, and table joins.
  * `03_gold_aggregations.ipynb`: Generates KPIs (e.g., total revenue per product, customer lifetime value).
  * `04_analytics_and_dashboard.ipynb`: Final queries and visual dashboard generation.

## 🛠️ Tech Stack
* **Engine**: Azure Databricks, PySpark
* **Storage**: Delta Lake, Cloud Object Storage
* **Design Pattern**: Medallion Architecture
