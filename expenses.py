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
         

    expense = {"name": expense_name, "category": category, "amount": amount}
    return expense

    