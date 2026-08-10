# Expense Tracker...!!

expenseslist = []  #list of all Expenses

print ("Welcome to the Expense Tracker..!!")

while True:
    print ("=== Menu ===")
    print ("1. Add Expense")
    print ("2. view Expenses")
    print ("3.View Total Expenses")
    print ("4. To Exit")

    choise = int(input("Enter your choise :"))

# Add Expense

    if choise == 1:
        date = input("Enter the date (DD-MM-YYYY): ")
        category = input("Enter the category: ")
        discription = input("Enter the description: ")
        amount = float(input("Enter the amount : "))

        expense = {
            "date": date,
            "category": category,
            "description": discription,
            "amount": amount
        }

        expenseslist.append(expense)
        print("\nDone ...!! Expense Added Successfully..!!\n")

# View Expenses

    elif choise == 2:
        if len(expenseslist) == 0:
            print ("\n No Expenses Added Yet..!!\n")
        else:
            print("\n=== Expenses ===")
            count = 1
            for expense in expenseslist:
                print(f"Expense Number{count} -> Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']}")
                count += 1

# View Total Expenses

    elif choise == 3:
        total = 0
        for expense in expenseslist:
            total += expense['amount']

        print("\nTotal Expenses: ", total, "\n")

# Exit

    elif choise == 4:
        print("\nThank You for using Expense Tracker..!!\n")
        break

    else:
        print("\nInvalid Choice..!! Please try again..!!\n")