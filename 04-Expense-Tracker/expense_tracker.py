# 04-Expense-Tracker/expense_tracker.py
import csv
from datetime import date

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
    """Print all expenses nicely"""
    if not expenses:
        print("No expenses yet!")
        return
    
    total = 0
    print("\n=== All Expenses ===")
    for e in expenses:
        print(f"{e['date']} | {e['category']:<12} | ${e['amount']:.2f} | {e['note']}")
        total += e['amount']
    print(f"\nTOTAL SPENT: ${total:.2f}")

def main():
    print("Personal Expense Tracker")
    expenses = load_expenses()  # ← Loads old data!
    
    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. Quit")
        choice = input("Choose (1-3): ")
        
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)   # ← Saves every time!
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print("Goodbye! Your data is saved.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()