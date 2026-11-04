
expenseslist = []

print("Welcome to the Expense Tracker..!!")


# Menu Function
def menu():
    print("\n=== Menu ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        return 0


# Add Expense Function
def add_expense(expenseslist):

    date = input("Enter the date (DD-MM-YYYY): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")

    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Please enter a valid amount!")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenseslist.append(expense)

    print("\nDone...!! Expense Added Successfully..!!")


# View Expenses Function
def view_expenses(expenseslist):

    if len(expenseslist) == 0:
        print("\nNo Expenses Added Yet..!!")

    else:
        print("\n=== Expenses ===")

        count = 1

        for expense in expenseslist:

            print(
                f"Expense Number {count} -> "
                f"Date: {expense['date']}, "
                f"Category: {expense['category']}, "
                f"Description: {expense['description']}, "
                f"Amount: ₹{expense['amount']:.2f}"
            )

            count += 1


# View Total Expenses Function
def view_total_expenses(expenseslist):

    total = 0

    for expense in expenseslist:
        total += expense['amount']

    print("\nTotal Expenses: ₹", total)


# Main Expense Tracker Function
def expense_tracker():

    while True:

        choice = menu()

        if choice == 1:
            add_expense(expenseslist)

        elif choice == 2:
            view_expenses(expenseslist)

        elif choice == 3:
            view_total_expenses(expenseslist)

        elif choice == 4:
            print("\nThank You for using Expense Tracker..!!")
            break

        else:
            print("\nInvalid Choice..!! Please try again..!!")


expense_tracker()
