
import time
from expenses import get_expense, display_expenses, save_expenses, load_expenses, calculate_total, calculate_category_totals


expenses = load_expenses()

while True:
    print(f"\n{"-"*30}Expense Tracker{"-"*30} \n1. Add Expense \n2. View Expenses \n3. Save and Exit\n{"-"*75}")
    choice = input("\nPlease select an option (1-3): ").strip()

    match choice:
        case "1":
            expense = get_expense()
            expenses.append(expense)
        case "2":
            display_expenses(expenses)
            total_expenses = calculate_total(expenses)
            category_totals = calculate_category_totals(expenses)
            print(f"\nTotal Expenses; ${total_expenses:.2f}")
            print(f"\nCategory Totals: ")
            for category, total in category_totals:
                print(f"{category}: ${total:.2f}")
            print("\n" + "-"*78)
            input("Press any key to return to the main menu: ")
        case "3":
            save_expenses(expenses)
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please select a valid option (1-3).")
            time.sleep(2) # Pause for 2 seconds before returning to the main menu
