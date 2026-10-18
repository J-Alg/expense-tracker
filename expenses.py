import json
from datetime import date

def main_menu():
    print("\nExpense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Save and Exit")
    choice = input("Please select an option (1-3): ").strip()
    return choice

def view_expenses_menu():
    print("\nView Expenses Menu")
    print("1. View All Expenses")
    print("2. Filter Expenses by Category")
    print("3. Return to Main Menu")

    menu_choice = input("Please select an option (1-3): ").strip()
    return menu_choice
    

def load_expenses(filename="expenses.json"):
    try: 
        with open(filename, "r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        return []

def get_expense():
    expense_name = input("Please enter expense name: ").strip().title()

    category = input("What category are you assigning this expense to (e.g Food, Mortgage, Misc)? ").strip().title()

    while True:
        try:
            new_amount = input("Expense Value: ")
            amount = float(new_amount)
            if amount > 0:
                break
            else:
                print("Please enter value greater than 0")
                continue
        except ValueError:
            print("Enter expense as decimal value (ex: 25.00)")
            continue

    expense_date = date.today().strftime("%Y-%m-%d") 


    expense = {"name": expense_name, "category": category, "amount": amount, "date": expense_date}
    return expense


def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"\n{"-"*30}Recorded Expenses{"-"*30}")
    for expense in expenses:
        print(f"\nExpense: {expense['name']}\nCategory: {expense['category']}\nAmount:${expense['amount']:.2f}\nDate: {expense['date']}")

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    return total

def calculate_category_totals(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return sorted(category_totals.items(), key=lambda x: x[1], reverse=True)

def filter_expenses_by_category(expenses, category):
    filtered_expenses = [expense for expense in expenses if expense["category"].lower() == category.lower()]
    return filtered_expenses
    