# 04-Expense-Tracker/expense_tracker.py
import csv
from datetime import date
from collections import defaultdict # for default dictionary which auto creats missing key
import os   # for checking file existence

# File where we save everything
FILE_NAME = "expenses.csv"

def load_expenses():
    """Read all old expenses from the file when program starts"""
    expenses = []
    try:
        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)   # File ma haleko data lai dictionary ko rup ma read garne
            for row in reader:      
                                    # row["date"] → "2025-04-05"
                                    # row["amount"] → "12.50" (string → we convert to float)
                row["amount"] = float(row["amount"])  #  amount ma vako data lai float ma convert garne
                expenses.append(row)    # dictionary lai list ma add garne
        print(f"Loaded {len(expenses)} old expenses!")  # kati ota expense load bhayo bhanera print garne
    except FileNotFoundError:
        print("No old expenses found – starting fresh!")
    return expenses

def save_expenses(expenses):
    """Save all expenses to the file"""
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["date", "category", "amount", "note"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)    # create writer object jasle dictionary lai csv ma convert garne
        writer.writeheader()    # writes the first line: date,category,amount,note
        writer.writerows(expenses)  # writes all our dictionaries as rows

def add_expense(expenses):
    """Ask user for new expense and add it"""
    print("\n--- Add New Expense ---")
    amount = float(input("Amount (e.g. 12.50): "))
    category = input("Category (food/transport/entertainment/etc): ").strip()
    note = input("Note (optional): ").strip()
    
    expense = {
        "date": date.today().isoformat(),
        "category": category,
        "amount": amount,
        "note": note
    }
    expenses.append(expense)
    print("Expense added!")

def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet!\n")
        return
    
    print("="*60)   # table header banako
    print(f"{'#':<3} {'Date':<12} {'Category':<15} {'Amount':>8}  {'Note'}")
    print("-"*60)
    
    total = 0
    for i, e in enumerate(expenses, 1): # enumerate le index (i) ra element (e) return garcha, 1 bata start garne indexing
        print(f"{i:<3} {e['date']:<12} {e['category']:<15} ${e['amount']:>7.2f}  {e['note']}")  # e['key'] → access values in each expense dictionary.
                                                                                                # ${e['amount']:>7.2f} → formats the amount as currency with 2 decimal places, right-aligned.
        total += e['amount']
    
    print("-"*60)   # Prints a separator line.
                    # Displays the total expense nicely formatted.
    print(f"{'TOTAL':<38} ${total:>7.2f}\n")

def show_summary(expenses):
    if not expenses:
        print("No data to summarize!\n")
        return
    
    # Category totals
    by_category = defaultdict(float)
    for e in expenses:
        by_category[e['category']] += e['amount']
    
    print("SUMMARY BY CATEGORY")
    print("-" * 40)
    for cat, amt in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat.capitalize():<20} ${amt:>8.2f}")
    print("-" * 40)
    
    # This month only
    this_month = date.today().strftime("%Y-%m")
    monthly_total = sum(e['amount'] for e in expenses if e['date'].startswith(this_month))
    print(f"This month ({this_month}): ${monthly_total:.2f}\n")

def delete_expense(expenses):
    show_expenses(expenses)
    if not expenses:
        return
    
    try:
        idx = int(input("Enter # of expense to delete (or 0 to cancel): ")) - 1
        if idx < 0 or idx >= len(expenses):
            print("Invalid number!")
            return
        removed = expenses.pop(idx)
        print(f"Deleted: ${removed['amount']} on {removed['date']} ({removed['category']})")
    except ValueError:
        print("Invalid input!")

def main():
    print("Personal Expense Tracker v2".center(50, "="))
    expenses = load_expenses()
    
    while True:
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View summary")
        print("4. Delete expense")
        print("5. Quit")
        choice = input("\nChoose (1-5): ").strip()
        
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
            save_expenses(expenses)
        elif choice == "5":
            print("Goodbye! All data saved.")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()