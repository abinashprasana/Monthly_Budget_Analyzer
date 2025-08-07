# 💰 Monthly Budget Analyzer

A simple and insightful Python project that helps analyze your monthly expenses by reading multiple CSV files (January, February, March) from a ZIP archive and generating a clean expense summary table and a colorful bar chart based on spending categories. Perfect for personal budgeting or educational use! 📈📊

---

## 🔑 Key Features

- 📦 Automatically extracts and processes zipped CSV data  
- 📁 Combines multiple monthly datasets into one DataFrame  
- 🧠 Generates a pivot summary table for better clarity  
- 📊 Visualizes monthly expenses by category using a bar chart  
- 🧹 Cleans and validates numeric data for reliable analysis  

---

## 💡 Benefits

- 📉 Helps understand where your money is going  
- 🧠 Strengthens your understanding of Pandas, Matplotlib, and data manipulation  
- ⚙️ Real-world use case to practice file I/O and data visualization  
- 🧑‍💻 Great for beginner to intermediate Python learners looking to build a practical project  

---

## 🧠 Concepts Used

- 🗂️ Python File Handling (`os`, `zipfile`)  
- 📊 Data Analysis with **Pandas**  
- 🧼 Data Cleaning & Validation  
- 📂 CSV Parsing & Combining  
- 🧾 Pivot Tables  
- 🎨 Data Visualization with **Matplotlib**  

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

## ▶️ How to Run the Program

1. ✅ Ensure you have Python installed.  
2. 🔧 Install required packages if not already installed:
   ```
   pip install pandas matplotlib
   ```
3. 🚀 Run the script using:
   ```
   python main.py
   ```

✅ The script will:
- 📂 Extract the ZIP file (`monthly_budget_data.zip`)
- 🔄 Combine monthly CSVs
- 🧾 Print an expense summary table
- 📊 Show a bar chart of category-wise monthly spending

---

## 📌 Output

### 📋 Expense Summary Table

![Expense Summary Table](Screenshots/Expense_Summary_Table.png)

### 📊 Monthly Expense Chart

![Monthly Expense Chart](Screenshots/Monthly_Expense_Chart.png)

---

## 👨‍💻 Author

Created with ❤️ by **Abinash Prasana**

---
