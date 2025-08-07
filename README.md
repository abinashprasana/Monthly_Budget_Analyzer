# 💰 Monthly Budget Analyzer

**Monthly Budget Analyzer** is a Python CLI tool for analyzing and visualizing your monthly expenses. It reads multiple CSV files (e.g., January, February, March) from a ZIP archive, processes and cleans the data, and generates both a summary table and a colorful bar chart of your spending categories. This project is perfect for personal budgeting, educational practice, or honing your Python skills! 📈📊

---

## 🔑 Key Features

- 📦 **Automated ZIP extraction:** Easily loads and processes zipped CSV files.
- 📁 **Multi-month data merging:** Combines several monthly datasets into a single, unified DataFrame.
- 🧠 **Pivot summary table:** Creates clear, categorized expense summaries for deeper insight.
- 📊 **Category-wise visualization:** Plots interactive bar charts of your expenses by category.
- 🧹 **Robust data cleaning:** Ensures reliable analysis with validation and cleaning of numeric data.

---

## 💡 Benefits

- 📉 Quickly see where your money goes each month.
- 🧠 Sharpen your skills in Pandas, Matplotlib, and real-world data manipulation.
- ⚙️ Practice file handling and data visualization for practical use cases.
- 🧑‍💻 Suitable for beginner and intermediate Python learners.

---

## 🧠 Concepts Used

- 🗂️ **Python File Handling:** (`os`, `zipfile`)
- 📊 **Data Analysis:** with **Pandas**
- 🧼 **Data Cleaning & Validation**
- 📂 **CSV Parsing & Merging**
- 🧾 **Pivot Tables**
- 🎨 **Visualization:** with **Matplotlib**

---

## 📁 File Structure

```
Monthly_Budget_Analyzer/
├── main.py
├── monthly_budget_data.zip
├── data/
│   ├── january.csv
│   ├── february.csv
│   └── march.csv
├── Screenshots/
│   ├── Expense_Summary_Table.png
│   └── Monthly_Expense_Chart.png
```

---

## ▶️ How to Run

1. ✅ Make sure Python is installed.
2. 🔧 Install dependencies:
   ```
   pip install pandas matplotlib
   ```
3. 🚀 Run the script:
   ```
   python main.py
   ```

The script will:
- 📂 Extract the ZIP file (`monthly_budget_data.zip`)
- 🔄 Merge the monthly CSVs
- 🧾 Print an expense summary table
- 📊 Display a bar chart of category-wise monthly spending

---

## 📌 Output

### 📋 Expense Summary Table
![📋 Expense Summary Table](Monthly%20Budget%20Analyzer/Screenshots/Expense_Summary_Table.png)

### 📊 Monthly Expense Chart
![📊 Monthly Expense Chart](Monthly%20Budget%20Analyzer/Screenshots/Monthly_Expense_Chart.png)
---

## 👨‍💻 Author

**Abinash Prasana**

---

Let me know if you want any further customization or want to add sections like “Contributing,” “License,” or “Troubleshooting”!
