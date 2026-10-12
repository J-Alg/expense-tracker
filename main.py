
from expenses import get_expense, display_expenses, save_expenses

expenses = []

while True:
    print("Menu: \n1. Add Expense \n2. View Expenses \n3. Save and Exit")
    choice = input("Please select an option (1-3): ").strip()

    if choice == "1":
        expense = get_expense()
        expenses.append(expense)
    elif choice == "2":
        display_expenses(expenses)
        input("\nPress any key to return to the main menu: ")
    elif choice == "3":
        save_expenses(expenses)
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-3).")