
import time
from expenses import get_expense, display_expenses, main_menu, save_expenses, load_expenses, filter_expenses_by_category, view_expenses_menu


expenses = load_expenses()

while True:
    choice = main_menu()
    match choice:
        case "1":
            expense = get_expense()
            expenses.append(expense)
        case "2":
            menu_choice = view_expenses_menu()
            match menu_choice:
                case "1":
                    display_expenses(expenses)
                    input("\nPress Enter to return to the main menu... ")

                case "2":
                    category = input("Enter the category to filter by: ")
                    filtered_expenses = filter_expenses_by_category(expenses, category)
                    display_expenses(filtered_expenses)
                    input("\nPress Enter to return to the main menu... ")
                case "3":
                    print("Returning to the main menu...")
                    continue
                case _:
                    print("Invalid Choice. Returning to the main menu...")
                    time.sleep(1)
        case "3":
            save_expenses(expenses)
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please select a valid option (1-3).")
            time.sleep(2) # Pause for 2 seconds before returning to the main menu
