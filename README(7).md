# 📚 Library Dashboard

A Python-based **Library Dashboard** that reads library transaction data from a CSV file, calculates useful statistics, filters transactions by genre, and generates visual reports.

## ✨ Features

- 📥 Load library data from a CSV file using Pandas
- 🔍 Check and remove missing values
- 📊 Find the most borrowed book
- ⏱️ Calculate the average borrowing duration
- 📅 Find the busiest borrowing day
- 🎭 Filter transactions by genre
- 📈 Generate a statistical summary
- 📊 Display the Top 5 Borrowed Books
- 📉 Show monthly borrowing trends
- 🥧 Display genre distribution
- 🔥 Show borrowing activity by day and hour using a heatmap

## 🛠️ Technologies Used

- Python 🐍
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📁 Project Files

```text
Library Dashboard/
│
├── index.py
├── library_data.csv
└── README.md
```

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

## ▶️ How to Run

1. Keep `index.py` and `library_data.csv` in the same folder.
2. Open Command Prompt, Terminal, or VS Code in that folder.
3. Run:

```bash
python index.py
```

The program loads `library_data.csv`, calculates statistics, filters Fiction transactions, and generates charts.

## 📊 Main Statistics

The program calculates:

- **Most Borrowed Book**
- **Average Borrowing Duration**
- **Busiest Day**

The source code uses the columns `Book Title`, `Borrowing Duration (Days)`, `Date`, `Genre`, and `Transaction ID`.

## 📈 Generated Reports

The dashboard generates these visualizations:

1. 📚 Top 5 Borrowed Books
2. 📅 Borrowing Trends Over Months
3. 🎭 Genre Distribution
4. 🔥 Borrowing Activity by Day & Hour

## 🔎 Example Filter

The program includes an example Fiction filter:

```python
dashboard.filter_transactions(genre="Fiction")
```

You can change `"Fiction"` to another genre available in your CSV file.

## 🖼️ Output Screenshots

Add your program output screenshots here:

### 📊 Statistics Output

> Add screenshot here

### 📈 Charts / Dashboard Output

> Add screenshot here

## 📝 Notes

Make sure `library_data.csv` contains the required column names before running the program.

## 👨‍💻 Author

**Vraj Jetani**

---
⭐ If you find this project useful, consider giving it a star!
