import time
from expenses import get_expense, display_expenses, save_expenses, load_expenses, filter_expenses_by_category, calculate_total, calculate_category_totals

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
    print("3. View Total Expenses by Category")
    print("4. Return to Main Menu")

    menu_choice = input("Please select an option (1-4): ").strip()
    return menu_choice

def return_to_main_menu():
    input("\nPress Enter to return to the main menu... ")

expenses = load_expenses()

while True:
    choice = main_menu()
    match choice:
        case "1":
            expense = get_expense()
            expenses.append(expense)
            return_to_main_menu()           
        case "2":
            menu_choice = view_expenses_menu()
            match menu_choice:
                case "1":
                    display_expenses(expenses)
                    total_expenses = calculate_total(expenses)
                    print(f"\nTotal of all expenses ${total_expenses:.2f}")
                    return_to_main_menu()
                case "2":
                    category = input("Enter the category to filter by: ")
                    filtered_expenses = filter_expenses_by_category(expenses, category)
                    if not filtered_expenses:
                        print(f"\nNo expenses found for category: {category.title()}")
                    else:
                        display_expenses(filtered_expenses)
                        filter_total = calculate_total(filtered_expenses)
                        print(f"\n{category.title()} Total: ${filter_total:.2f}")
                    return_to_main_menu()
                case "3":
                    category_totals = calculate_category_totals(expenses)
                    print("\nCategory Totals:")
                    for category, total in category_totals:
                        print(f"{category}: ${total:.2f}")
                    return_to_main_menu()  
                case "4":
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
