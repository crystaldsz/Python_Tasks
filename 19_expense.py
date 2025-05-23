#Expense Tracker 
#Input daily expenses and generate a weekly summary (store data in a file or dictionary). 

import json
from datetime import datetime, timedelta
EXPENSE_FILE = 'expenses.json'

def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {} 

def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as f:
        json.dump(expenses, f, indent=4) 

def add_expense(expenses):
    date_str = input("Enter date (YYYY-MM-DD, leave blank for today): ")
    if not date_str:
        date = datetime.now().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date_str, '%Y-%m-%d') 
            date = date_str
        except ValueError:
            print("Invalid date format. Using today's date.")
            date = datetime.now().strftime('%Y-%m-%d')

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    category = input("Enter category (e.g., food, transport, entertainment): ").lower()
    description = input("Enter description (optional): ")

    if date not in expenses:
        expenses[date] = []
    expenses[date].append({
        'amount': amount,
        'category': category,
        'description': description
    })
    save_expenses(expenses)
    print("Expense added successfully!")

def get_week_range(start_date_str=None):
    
    if start_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format for summary. Using current week.")
            start_date = datetime.now()
    else:
        start_date = datetime.now()

    week_start = start_date - timedelta(days=start_date.weekday())
    week_end = week_start + timedelta(days=6)
    return week_start.strftime('%Y-%m-%d'), week_end.strftime('%Y-%m-%d')

def generate_weekly_summary(expenses):
    summary_date_str = input("Enter a date within the week you want to summarize (YYYY-MM-DD, leave blank for current week): ")
    week_start_str, week_end_str = get_week_range(summary_date_str)

    print(f"\n--- Weekly Summary ({week_start_str} to {week_end_str}) ---")

    total_weekly_expense = 0
    category_summary = {}
    detailed_expenses = []

    for date_str, daily_expenses in expenses.items():
        if week_start_str <= date_str <= week_end_str:
            for expense in daily_expenses:
                total_weekly_expense += expense['amount']
                category = expense['category']
                category_summary[category] = category_summary.get(category, 0) + expense['amount']
                detailed_expenses.append(f"{date_str}: ${expense['amount']:.2f} ({expense['category']}) - {expense['description']}")

    if not detailed_expenses:
        print("No expenses recorded for this week.")
        return

    print(f"Total Weekly Spending: ${total_weekly_expense:.2f}")

    print("\nSpending by Category:")
    for category, amount in sorted(category_summary.items(), key=lambda item: item[1], reverse=True):
        print(f"- {category.capitalize()}: ${amount:.2f}")

    print("\nDetailed Expenses for the Week:")
    for entry in detailed_expenses:
        print(entry)
    print("-----------------------------------")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add a new expense")
        print("2. Generate weekly summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            generate_weekly_summary(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()