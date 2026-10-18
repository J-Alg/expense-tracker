
import time
from expenses import get_expense, display_expenses, save_expenses, load_expenses, calculate_total, calculate_category_totals, filter_expenses_by_category


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
            print(f"\nTotal Expenses: ${total_expenses:.2f}")
            print(f"\nCategory Totals: ")
            for category, total in category_totals:
                print(f"{category}: ${total:.2f}")
            print("\n" + "-"*78)
            menu_choice = input("Would you like to: \n1. Add another expense? \n2. Filter expenses by category \n3. Return to Main Menu \nPlease select an option (1-2): ").strip()
            match menu_choice:
                case "1":
                    expense = get_expense()
                    expenses.append(expense)
                case "2":
                    filter_category = input("Enter the category to filter by: ").strip().lower()
                    filtered_expenses = filter_expenses_by_category(expenses, filter_category)
                    display_expenses(filtered_expenses)
                case "3":
                    continue       
                case _:
                    print("Invalid choice. Returning to the main menu.")
                    time.sleep(1) # Pause for 1 second before returning to the main menu
                    continue
        case "3":
            save_expenses(expenses)
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please select a valid option (1-3).")
            time.sleep(2) # Pause for 2 seconds before returning to the main menu
