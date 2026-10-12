
from expenses import get_expense, display_expenses, save_expenses, load_expenses, calculate_total

expenses = load_expenses()

while True:
    print(f"\n{"-"*30}Expense Tracker{"-"*30} \n1. Add Expense \n2. View Expenses \n3. Save and Exit\n{"-"*75}")
    choice = input("\nPlease select an option (1-3): ").strip()

    if choice == "1":
        expense = get_expense()
        expenses.append(expense)
    elif choice == "2":
        display_expenses(expenses)
        total_expenses = calculate_total(expenses)
        print(f"\nTotal Expenses: ${total_expenses:.2f}")
        print("\n" + "-"*78)
        input("Press any key to return to the main menu: ")
    elif choice == "3":
        save_expenses(expenses)
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-3).")

