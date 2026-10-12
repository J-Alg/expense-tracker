
from expenses import get_expense, display_expenses

expenses = []

while True:
    choice = input("Add a new expense (y/n)? ").strip().lower()

    if choice not in ("y", "yes", "n", "no"):
        print("Invalid input please enter 'y' or 'n'.")
        continue
    elif choice in ("n", "no"):
        break

    expense = get_expense()
    expenses.append(expense)
display_expenses(expenses)