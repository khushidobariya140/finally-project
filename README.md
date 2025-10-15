# finally-project
Retail Sales Data Analyzer
Overview

The Retail Sales Data Analyzer is a Python command-line application that helps businesses analyze their sales data. It allows you to:

Load sales data from a CSV file

Validate and clean the dataset

Calculate key metrics like total sales, average sale value, and most popular product

Filter sales data by category or date range

Generate insightful visualizations including bar charts, line charts, histograms, and scatter plots

Features

Load Sales Data

Load a CSV file containing sales information.

Automatically handles missing or invalid data.

Summary Report

Calculates:

Total sales

Average sale value

Most popular product by quantity sold

Data Filtering

Filter sales data based on:

Product category

Date range

Data Visualization

Bar chart of total sales by category

Line chart of sales trend over time

Histogram of product prices

Scatter plot of price vs quantity sold

Requirements

Python 3.8+

Libraries:

pandas

numpy

matplotlib

seaborn

Install dependencies via:

pip install pandas numpy matplotlib seaborn

Usage

Place your sales CSV file (e.g., retail_sales.csv) in the same folder as retail4.py.

Run the script:

python retail4.py


Follow the menu:

1. Load Sales Data
2. Display Summary Report
3. Filter and View Data
4. Generate Visualizations
5. Exit


Input the required options as prompted.

CSV Format

The CSV file must contain the following columns:

Column	Type	Description
Date	YYYY-MM-DD	Date of sale
Product	string	Product name
Category	string	Product category (e.g., Electronics, Clothing)
Price	float	Price per unit
Quantity Sold	int	Number of units sold

Example:

Date,Product,Category,Price,Quantity Sold
2025-10-01,Apple iPhone,Electronics,999,5
2025-10-02,Samsung TV,Electronics,499,2
2025-10-03,Levi's Jeans,Clothing,59,10

Notes

Invalid or missing rows are automatically removed during loading.

The script calculates Total Sales automatically if the column is missing.

Visualizations are displayed using matplotlib and seaborn.

Author

Khushi Dobariya
