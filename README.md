# 📈 Stock Portfolio Tracker (Console Version)

A console-based stock portfolio tracker built with Python. This version allows users to enter stock symbols and quantities manually and view their total investment.

## ✅ Features

- 📦 5 predefined stock symbols (AAPL, TSLA, GOOGL, MSFT, AMZN)
- 🧮 Calculates total investment based on quantity entered
- 💾 Option to save investment summary to a `.txt` file
- 🧑‍💻 Runs entirely in the terminal — great for quick use

## 📷 How It Looks

Enter stock symbol (AAPL/TSLA/...): AAPL  
Enter quantity: 5  
Do you want to add another stock? (yes/no): no  

Total Investment: ₹98765  
Do you want to save the result? (yes/no): yes  
Result saved as investment_summary.txt

## ▶️ How to Run

Make sure you have **Python 3** installed.

Open terminal or VS Code and run:

```bash
python stock_tracker_console.py
🧠 Concepts Used
1. Dictionaries for stock symbols and prices
2. Loops and conditionals for input control
3. User input validation
4. String formatting and calculations
5. File handling for saving summaries

🧾 Requirements
Python 3.x

No external libraries needed (only standard library)

📂 File Structure

stock_tracker_console/
├── stock_tracker_console.py
└── README.md
