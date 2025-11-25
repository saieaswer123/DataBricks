📦 E-Commerce Data Engineering Pipeline (Databricks, PySpark, Delta Lake)

This project demonstrates a complete end-to-end ELT Data Engineering pipeline using Databricks, PySpark, Delta Lake, and Unity Catalog.
The pipeline follows the industry-standard Bronze → Silver → Gold architecture and includes full data ingestion, transformations, aggregations, and dashboards for analytics.

🚀 Project Overview

This project simulates an E-Commerce Analytics Platform.
It processes sales, customer, and product data using Databricks notebooks and generates actionable insights through dashboards.

✔ Key Features

Ingest raw CSV files from Unity Catalog Volumes

Store cleaned data in Delta tables

Apply transformations using PySpark

Build Gold-level analytics tables (Daily Sales, Top Products, LTV)

Create fully interactive Databricks SQL Dashboards

Orchestrate pipeline using Databricks Jobs / Workflows

🛠️ Tech Stack
Component	Technology
Cloud Platform	Databricks
Storage	Unity Catalog Volumes
Processing	PySpark
Format	Delta Lake
Orchestration	Databricks Workflows
Visualization	Databricks SQL
📁 Folder Structure
📦 ecommerce-data-pipeline
 ┣ 📂 data
 ┃ ┣ orders_big.csv
 ┃ ┣ customers_big.csv
 ┃ ┗ products_big.csv
 ┣ 📂 notebooks
 ┃ ┣ 01_bronze_ingestion.py
 ┃ ┣ 02_silver_transformations.py
 ┃ ┣ 03_gold_aggregations.py
 ┃ ┗ 00_run_full_pipeline.py
 ┣ 📄 README.md

📊 Architecture (Bronze, Silver, Gold)
1️⃣ Bronze Layer – Raw Ingestion

Reads CSV from Volumes

Adds ingestion metadata

Stores raw data as Delta tables

Tables:

bronze_orders

bronze_customers

bronze_products

2️⃣ Silver Layer – Data Cleaning & Enrichment

Type casting

Null handling

Removing duplicates

Normalizing text fields

Tables:

silver_orders

silver_customers

silver_products

3️⃣ Gold Layer – Business-Level Aggregations

Creates analytics-ready datasets:

Daily Sales

Top Products

Customer Lifetime Value (LTV)

Country-wise Sales

Tables:

gold_daily_sales

gold_top_products

gold_customer_ltv

gold_country_sales

📥 Input Data (CSV files)

You will upload these files to:

/Volumes/<catalog>/<schema>/raw/orders/


Your data includes:

300-row orders dataset

40 customers

30 products

Generated using Python and included in the repo.

📓 Notebooks
01_bronze_ingestion

Reads raw CSV files

Writes Delta Bronze tables

02_silver_transformations

Cleans & transforms Bronze data

Writes Delta Silver tables

03_gold_aggregations

Joins Silver tables

Creates Gold aggregated datasets

00_run_full_pipeline

Executes the complete ELT pipeline using %run commands

🔄 Pipeline Orchestration

Use Databricks Workflows:

✔ Task 1: bronze_task

Runs: 01_bronze_ingestion

✔ Task 2: silver_task

Runs after Bronze
Notebook: 02_silver_transformations

✔ Task 3: gold_task

Runs after Silver
Notebook: 03_gold_aggregations

You can schedule:

Daily

Hourly

Weekly
or run manually.

📊 Dashboards (Databricks SQL)

Dashboards built from Gold tables include:

Daily Sales Tracking

Revenue trend

Orders per day

Customer count

Top Products Analysis

Highest revenue generators

Most sold products

Customer LTV Dashboard

High-value customers

Total items bought

Country Sales Dashboard

Revenue by country

Orders by geography

🧑‍💻 How to Run the Project
Step 1: Upload CSV Files

Upload to Volumes:

/Volumes/main/ecommerce/raw/orders/

Step 2: Run Bronze Notebook
Step 3: Run Silver Notebook
Step 4: Run Gold Notebook
Step 5: Build Dashboards in Databricks SQL
Step 6: Create Workflow and Automate
🏆 Final Output

Fully automated ELT pipeline in Databricks

Clean Delta tables in SQL

Interactive dashboards

Ready-to-use portfolio-grade Data Engineering project
