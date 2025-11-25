# Databricks notebook source
from pyspark.sql.functions import current_timestamp
orders_df_raw = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load("/Volumes/ecommerce_project_1/ecommerce_project_1/raw/orders_big.csv")
    .withColumn("ingest_ts", current_timestamp())
)

# Read customers
customers_df_raw = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load("/Volumes/ecommerce_project_1/ecommerce_project_1/raw/customers_big.csv")
    .withColumn("ingest_ts", current_timestamp())
)

# Read products
products_df_raw = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load("/Volumes/ecommerce_project_1/ecommerce_project_1/raw/products_big.csv")
    .withColumn("ingest_ts", current_timestamp())
)

# COMMAND ----------

display(orders_df_raw.limit(5))

# COMMAND ----------

display(customers_df_raw.limit(5))

# COMMAND ----------

display(products_df_raw.limit(5))

# COMMAND ----------

(
orders_df_raw
    .write 
    .format("delta")
    .mode("overwrite")                # use "append" for incremental loads
    .option("overwriteSchema", "true")
    .saveAsTable("ecommerce_project_1.ecommerce_project_1.bronze_orders")

)

# COMMAND ----------

(
    customers_df_raw
    .write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("ecommerce_project_1.ecommerce_project_1.bronze_customers")
)

# COMMAND ----------

(
    products_df_raw
    .write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("ecommerce_project_1.ecommerce_project_1.bronze_products")
)


# COMMAND ----------

display(spark.table("ecommerce_project_1.ecommerce_project_1.bronze_orders").limit(5))

# COMMAND ----------

display(spark.table("ecommerce_project_1.ecommerce_project_1.bronze_customers").limit(5))

# COMMAND ----------

display(spark.table("ecommerce_project_1.ecommerce_project_1.bronze_products").limit(5))

# COMMAND ----------

