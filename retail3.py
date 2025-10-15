import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class RetailAnalyzer:
    def __init__(self):
        """Initializes the RetailAnalyzer with an empty DataFrame."""
        self.df = pd.DataFrame()
        self.metrics = {}

    def load_data(self, file_path="retail_sales.csv"):
        """
        Loads and validates the retail sales data from a CSV file.
        Performs initial cleaning and column creation.
        """
        # Check if file exists
        if not os.path.exists(file_path) or not file_path.endswith('.csv'):
            print(f"Error: File not found or is not a CSV file at '{file_path}'")
            return False

        # Read CSV
        self.df = pd.read_csv(file_path)

        # Required columns
        required_columns = ['Date', 'Product', 'Category', 'Price', 'Quantity Sold']
        missing_cols = [col for col in required_columns if col not in self.df.columns]
        if missing_cols:
            print(f"Error: CSV missing columns: {', '.join(missing_cols)}")
            self.df = pd.DataFrame()
            return False

        # Handle missing values by dropping rows with missing required data
        self.df.dropna(subset=required_columns, inplace=True)

        # Convert data types
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
        self.df['Price'] = pd.to_numeric(self.df['Price'], errors='coerce')
        self.df['Quantity Sold'] = pd.to_numeric(self.df['Quantity Sold'], errors='coerce')

        # Remove rows with invalid dates or numbers
        self.df.dropna(subset=['Date', 'Price', 'Quantity Sold'], inplace=True)

        # Generate 'Total Sales' if not present
        if 'Total Sales' not in self.df.columns:
            self.df['Total Sales'] = self.df['Price'] * self.df['Quantity Sold']

        print("Data loaded and processed successfully.")
        return True

    def calculate_metrics(self):
        """Calculates key metrics from the dataset using Pandas and NumPy."""
        if self.df.empty:
            print("No data loaded to calculate metrics.")
            return {}

        total_sales = np.sum(self.df['Total Sales'])
        average_sales = np.mean(self.df['Total Sales'])
        most_popular_product = self.df.groupby('Product')['Quantity Sold'].sum().idxmax()

        self.metrics = {
            'Total Sales': total_sales,
            'Average Sale Value': average_sales,
            'Most Popular Product': most_popular_product
        }
        return self.metrics

    def display_summary(self):
        """Displays a summary report of the analysis."""
        if self.df.empty:
            print("No data loaded. Please load data first.")
            return

        if not self.metrics:
            self.calculate_metrics()

        print("\n--- Retail Analysis Summary ---")
        print(f"Total Sales: ${self.metrics['Total Sales']:,.2f}")
        print(f"Average Sale Value: ${self.metrics['Average Sale Value']:,.2f}")
        print(f"Most Popular Product: {self.metrics['Most Popular Product']}")
        print("-----------------------------\n")

    def filter_data(self, category=None, start_date=None, end_date=None):
        """Filters data based on category and/or date range."""
        if self.df.empty:
            print("No data loaded to filter.")
            return pd.DataFrame()

        filtered_df = self.df.copy()
        if category:
            filtered_df = filtered_df[filtered_df['Category'].str.lower() == category.lower()]
        if start_date:
            filtered_df = filtered_df[filtered_df['Date'] >= pd.to_datetime(start_date)]
        if end_date:
            filtered_df = filtered_df[filtered_df['Date'] <= pd.to_datetime(end_date)]

        return filtered_df

    def visualize_data(self):
        """Creates insightful visualizations to analyze sales trends."""
        if self.df.empty:
            print("No data available for visualization.")
            return

        sns.set_theme(style="whitegrid")
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))
        fig.suptitle('Retail Sales Analysis Dashboard', fontsize=22)

        # Bar Chart: Total sales by category
        category_sales = self.df.groupby('Category')['Total Sales'].sum().sort_values(ascending=False)
        sns.barplot(ax=axes[0, 0], x=category_sales.index, y=category_sales.values, palette='plasma')
        axes[0, 0].set_title('Total Sales by Product Category', fontsize=14)
        axes[0, 0].set_xlabel('Category', fontsize=12)
        axes[0, 0].set_ylabel('Total Sales ($)', fontsize=12)
        axes[0, 0].tick_params(axis='x', rotation=45)

        # Line Graph: Sales trend over time
        daily_sales = self.df.groupby('Date')['Total Sales'].sum()
        sns.lineplot(ax=axes[0, 1], x=daily_sales.index, y=daily_sales.values, color='green', marker='o')
        axes[0, 1].set_title('Sales Trend Over Time', fontsize=14)
        axes[0, 1].set_xlabel('Date', fontsize=12)
        axes[0, 1].set_ylabel('Total Sales ($)', fontsize=12)
        axes[0, 1].tick_params(axis='x', rotation=45)

        # Histogram: Distribution of Product Prices
        sns.histplot(ax=axes[1, 0], data=self.df['Price'], kde=True, bins=20, color='skyblue')
        axes[1, 0].set_title('Distribution of Product Prices', fontsize=14)
        axes[1, 0].set_xlabel('Price ($)', fontsize=12)
        axes[1, 0].set_ylabel('Frequency', fontsize=12)

        # Scatter Plot: Price vs. Quantity Sold
        sns.scatterplot(ax=axes[1, 1], data=self.df, x='Price', y='Quantity Sold', hue='Category', palette='deep', alpha=0.7)
        axes[1, 1].set_title('Price vs. Quantity Sold', fontsize=14)
        axes[1, 1].set_xlabel('Price ($)', fontsize=12)
        axes[1, 1].set_ylabel('Quantity Sold', fontsize=12)

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()


def main():
    analyzer = RetailAnalyzer()

    while True:
        print("\n----- Retail Sales Data Analyzer Menu -----")
        print("1. Load Sales Data (from retail_sales.csv)")
        print("2. Display Summary Report")
        print("3. Filter and View Data")
        print("4. Generate Visualizations")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            file_path = input("Enter the path to the CSV file (default: retail_sales.csv): ").strip()
            if not file_path:
                file_path = "retail_sales.csv"
            success = analyzer.load_data(file_path)
            if success:
                analyzer.calculate_metrics()

        elif choice == '2':
            analyzer.display_summary()

        elif choice == '3':
            if analyzer.df.empty:
                print("Please load data first (Option 1).")
                continue
            category = input("Filter by category (or press Enter to skip): ").strip()
            start_date = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ").strip()
            end_date = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ").strip()

            filtered_data = analyzer.filter_data(
                category if category else None,
                start_date if start_date else None,
                end_date if end_date else None
            )

            if filtered_data.empty:
                print("\nNo results found for the given criteria.")
            else:
                print("\nFiltered Sales Data:")
                print(filtered_data.to_string())

        elif choice == '4':
            analyzer.visualize_data()

        elif choice == '5':
            print("Exiting the Retail Sales Analyzer. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
