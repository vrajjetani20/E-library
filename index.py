import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class LibraryDashboard:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
        
            self.data = pd.read_csv(self.file_path)

            
            print("Checking for missing values...")
            print(self.data.isnull().sum())

            self.data.dropna(inplace=True)

            print("Data loaded successfully!")
        except Exception as e:
            print("Error loading file:", e)

    def calculate_statistics(self):
        if self.data is None:
            print("No data loaded yet.")
            return

        most_borrowed = self.data['Book Title'].value_counts().idxmax()
        print("Most borrowed book:", most_borrowed)

        avg_duration = self.data['Borrowing Duration (Days)'].mean()
        print("Average borrowing duration:", round(avg_duration, 2), "days")

        busiest_day = self.data['Date'].value_counts().idxmax()
        print("Busiest day:", busiest_day)

    def filter_transactions(self, genre=None):
        if self.data is None:
            print("No data loaded yet.")
            return

        if genre:
            filtered = self.data[self.data['Genre'] == genre]
            print(f"Transactions for genre '{genre}':")
            print(filtered.head())
        else:
            print("No filter applied.")

    def generate_report(self):
        if self.data is None:
            print("No data loaded yet.")
            return

        print("\n--- Report Summary ---")
        print(self.data.describe())

        plt.figure(figsize=(10, 5))
        top_books = self.data['Book Title'].value_counts().head(5)
        top_books.plot(kind='bar', title="Top 5 Borrowed Books")
        plt.show()

        self.data['Date'] = pd.to_datetime(self.data['Date'])
        monthly_trend = self.data.groupby(self.data['Date'].dt.to_period("M")).size()
        monthly_trend.plot(kind='line', title="Borrowing Trends Over Months")
        plt.show()

        self.data['Genre'].value_counts().plot(kind='pie', autopct='%1.1f%%', title="Genre Distribution")
        plt.show()

        self.data['Day'] = self.data['Date'].dt.day_name()
        pivot = self.data.pivot_table(index='Day', columns=self.data['Date'].dt.hour, values='Transaction ID', aggfunc='count')
        sns.heatmap(pivot, cmap="YlGnBu")
        plt.title("Borrowing Activity by Day & Hour")
        plt.show()

if __name__ == "__main__":
    dashboard = LibraryDashboard("library_data.csv")
    dashboard.load_data()
    dashboard.calculate_statistics()
    dashboard.filter_transactions(genre="Fiction")  # Example filter
    dashboard.generate_report()
