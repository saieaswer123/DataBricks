# 📊 Superstore Sales Analysis

A data engineering and analytics project focused on processing the classic Superstore dataset to extract actionable retail insights.

## 📌 Project Overview
This project demonstrates the ability to take a raw, uncleaned sales dataset and transform it into a structured format for regional sales analysis, profit margin calculations, and inventory tracking.

## 📂 Contents
* **`First Project 2025-11-06.ipynb`**: The primary Databricks notebook containing the PySpark code for data extraction, transformation, and exploratory data analysis (EDA).
* **`superstore.csv`**: The raw dataset containing detailed transaction records, including order dates, shipping modes, customer segments, and geographical data.

## 🚀 Workflow
1. **Data Loading**: Ingesting `superstore.csv` into a PySpark DataFrame.
2. **Data Cleaning**: Handling missing values, standardizing date formats, and renaming columns for consistency.
3. **Analysis**: 
   * Calculating top-performing product categories.
   * Analyzing year-over-year sales growth.
   * Identifying regions with the highest profit margins.
4. **Storage**: Writing the cleaned, analytical tables back to storage in Delta format for high-performance querying.
