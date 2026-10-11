
from expenses import get_expense

expenses = []

while True:
    quit = input("Add a new expense (y/n)? ").strip().lower()
    choice = quit

    if choice not in ("y", "yes", "n", "no"):
        print("Invalid input please enter 'y' or 'n'.")
        continue
    elif choice in ("n", "no"):
        break

    expense = get_expense()
    expenses.append(expense)
print(expenses)
    